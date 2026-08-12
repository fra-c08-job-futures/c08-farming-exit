"""
CausalForestDML pipeline for two continuous treatments with heterogeneous
treatment effect (HTE) analysis, tree visualization, dose-response plots,
and SHAP-based feature importance.

Setup with uv:
    uv init causal-forest-project
    cd causal-forest-project
    uv add econml shap matplotlib pandas numpy scikit-learn
    uv run python causal_forest_pipeline.py

Data assumptions (edit the CONFIG section below to match your dataframe):
    - `outcome_col`      : single continuous outcome column
    - `treatment_cols`   : list of 2 continuous treatment columns
                            treat_A in [0, 1], treat_B in [0, 1000]
    - `het_cols`         : list of 5 columns used for heterogeneity (X)
    - `control_cols`     : list of 80 columns used only as controls (W)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shap

from sklearn.ensemble import RandomForestRegressor
from econml.dml import CausalForestDML
from econml.cate_interpreter import SingleTreeCateInterpreter

# --------------------------------------------------------------------------
# 0. CONFIG - point this at your real dataframe
# --------------------------------------------------------------------------
# df = pd.read_parquet("your_data.parquet")   # <-- load your real data here

outcome_col = "outcome"
treatment_cols = ["treat_A", "treat_B"]     # treat_A in [0,1], treat_B in [0,1000]
het_cols = [f"het_{i}" for i in range(5)]   # the 5 heterogeneity features (X)
control_cols = [f"ctrl_{i}" for i in range(80)]  # the 80 control-only features (W)

# --- synthetic stand-in so the script is runnable end to end; delete this
# block once you plug in your real dataframe above ---
np.random.seed(0)
n = 3000
X_ = pd.DataFrame(np.random.uniform(0, 1, size=(n, 5)), columns=het_cols)
W_ = pd.DataFrame(np.random.normal(size=(n, 80)), columns=control_cols)
T_A = np.random.uniform(0, 1, size=n)
T_B = np.random.uniform(0, 1000, size=n)
true_eff_A = 2 + 3 * X_["het_0"]
true_eff_B = 0.01 * (1 + X_["het_1"])
Y_ = (
    true_eff_A * T_A
    + true_eff_B * T_B
    + W_.iloc[:, :5].sum(axis=1) * 0.1
    + np.random.normal(scale=1.0, size=n)
)
df = pd.concat([X_, W_], axis=1)
df["treat_A"] = T_A
df["treat_B"] = T_B
df["outcome"] = Y_
# --- end synthetic block ---

Y = df[outcome_col].values
T = df[treatment_cols].values           # shape (n, 2), continuous
X = df[het_cols].values                 # heterogeneity features
W = df[control_cols].values             # controls only, no HTE slicing on these

# --------------------------------------------------------------------------
# 1. Fit CausalForestDML
# --------------------------------------------------------------------------
# With 2 continuous treatments, T is (n, 2) and discrete_treatment=False.
# model_y / model_t are the nuisance models used in the DML residualization
# step; swap these for gradient boosting etc. if that fits your data better.
est = CausalForestDML(
    model_y=RandomForestRegressor(
        n_estimators=200, min_samples_leaf=10, n_jobs=-1, random_state=0
    ),
    model_t=RandomForestRegressor(
        n_estimators=200, min_samples_leaf=10, n_jobs=-1, random_state=0
    ),
    discrete_treatment=False,
    n_estimators=1000,       # forest size for the causal forest itself
    min_samples_leaf=10,
    max_depth=None,
    cv=5,
    random_state=0,
    n_jobs=-1,
)

est.fit(Y=Y, T=T, X=X, W=W)
print("Model fit complete.")

# Sanity check: constant marginal effect at a few points -> shape (n_points, n_treatments)
print("const_marginal_effect example shape:", est.const_marginal_effect(X[:5]).shape)


# --------------------------------------------------------------------------
# 2. Tree-based visualization of treatment effects per group
# --------------------------------------------------------------------------
# SingleTreeCateInterpreter fits a shallow decision tree on X that explains
# *where in feature space* the (multi-dimensional) treatment effect is high
# or low, and shows the average effect for each leaf ("group").
intrp = SingleTreeCateInterpreter(
    include_model_uncertainty=False,
    max_depth=3,           # keep shallow so it stays readable
    min_samples_leaf=max(50, int(0.01 * len(df))),
)
intrp.interpret(est, X)

fig, ax = plt.subplots(figsize=(22, 10))
intrp.plot(
    ax=ax,
    feature_names=het_cols,
    treatment_names=treatment_cols,
    fontsize=10,
)
plt.tight_layout()
plt.savefig("cate_tree.png", dpi=150)
plt.close(fig)
print("Saved cate_tree.png")

# If you'd rather have crisp yes/no policy groups (e.g. "treat if effect > 0"),
# econml also has SingleTreePolicyInterpreter for that use case.


# --------------------------------------------------------------------------
# 3. Treatment <-> outcome relationship (dose-response curves)
# --------------------------------------------------------------------------
# Since treatments are continuous, "the effect" is a curve, not a single
# number. We trace out the average predicted effect of moving each
# treatment across its range while holding the other treatment fixed at
# its median observed value, using est.effect(X, T0=baseline, T1=grid).
def dose_response(est, X_eval, treatment_idx, grid, other_fixed_value, n_treatments=2):
    """Average effect of moving `treatment_idx` across `grid`, other treatment held fixed."""
    effects = []
    lb = []
    ub = []
    n_eval = X_eval.shape[0]
    for val in grid:
        T0 = np.zeros((n_eval, n_treatments))
        T1 = np.zeros((n_eval, n_treatments))
        T1[:, treatment_idx] = val
        other_idx = 1 - treatment_idx
        T0[:, other_idx] = other_fixed_value
        T1[:, other_idx] = other_fixed_value
        eff = est.effect(X_eval, T0=T0, T1=T1)
        try:
            lo, hi = est.effect_interval(X_eval, T0=T0, T1=T1, alpha=0.1)
            lb.append(lo.mean())
            ub.append(hi.mean())
        except Exception:
            lb.append(np.nan)
            ub.append(np.nan)
        effects.append(eff.mean())
    return np.array(effects), np.array(lb), np.array(ub)


X_eval = X[:500]  # subsample for speed; use full X if it's small enough

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

grid_A = np.linspace(df[treatment_cols[0]].min(), df[treatment_cols[0]].max(), 25)
eff_A, lo_A, hi_A = dose_response(
    est, X_eval, treatment_idx=0, grid=grid_A,
    other_fixed_value=np.median(df[treatment_cols[1]]),
)
axes[0].plot(grid_A, eff_A, color="C0")
if not np.isnan(lo_A).all():
    axes[0].fill_between(grid_A, lo_A, hi_A, alpha=0.2, color="C0")
axes[0].set_xlabel(treatment_cols[0])
axes[0].set_ylabel("Average predicted effect on outcome")
axes[0].set_title(f"Dose-response: {treatment_cols[0]}")

grid_B = np.linspace(df[treatment_cols[1]].min(), df[treatment_cols[1]].max(), 25)
eff_B, lo_B, hi_B = dose_response(
    est, X_eval, treatment_idx=1, grid=grid_B,
    other_fixed_value=np.median(df[treatment_cols[0]]),
)
axes[1].plot(grid_B, eff_B, color="C1")
if not np.isnan(lo_B).all():
    axes[1].fill_between(grid_B, lo_B, hi_B, alpha=0.2, color="C1")
axes[1].set_xlabel(treatment_cols[1])
axes[1].set_title(f"Dose-response: {treatment_cols[1]}")

plt.tight_layout()
plt.savefig("dose_response.png", dpi=150)
plt.close(fig)
print("Saved dose_response.png")

# Complementary view: distribution of individual-level CATEs (heterogeneity
# at a glance) for a fixed unit move in each treatment.
te_A = est.const_marginal_effect(X)[:, 0]
te_B = est.const_marginal_effect(X)[:, 1]
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(te_A, bins=40, color="C0")
axes[0].set_title(f"Marginal effect distribution: {treatment_cols[0]}")
axes[1].hist(te_B, bins=40, color="C1")
axes[1].set_title(f"Marginal effect distribution: {treatment_cols[1]}")
plt.tight_layout()
plt.savefig("effect_distribution.png", dpi=150)
plt.close(fig)
print("Saved effect_distribution.png")


# --------------------------------------------------------------------------
# 4. SHAP: which of the 5 heterogeneity features drive the treatment effect
# --------------------------------------------------------------------------
# CausalForestDML has native SHAP support: it explains the *predicted CATE*
# (not the outcome itself) as a function of X, separately per treatment.
shap_values = est.shap_values(
    X,
    feature_names=het_cols,
    treatment_names=treatment_cols,
)

# shap_values is a nested dict: {outcome_name: {treatment_name: Explanation}}
outcome_key = list(shap_values.keys())[0]  # single outcome -> "Y0"

for t_name in treatment_cols:
    exp = shap_values[outcome_key][t_name]
    plt.figure()
    shap.plots.beeswarm(exp, show=False)
    plt.title(f"SHAP: drivers of heterogeneity in effect of {t_name}")
    plt.tight_layout()
    plt.savefig(f"shap_beeswarm_{t_name}.png", dpi=150)
    plt.close()
    print(f"Saved shap_beeswarm_{t_name}.png")

    plt.figure()
    shap.plots.bar(exp, show=False)
    plt.title(f"SHAP importance: {t_name}")
    plt.tight_layout()
    plt.savefig(f"shap_bar_{t_name}.png", dpi=150)
    plt.close()
    print(f"Saved shap_bar_{t_name}.png")

print("\nDone. Outputs: cate_tree.png, dose_response.png, effect_distribution.png, "
      "shap_beeswarm_<treatment>.png, shap_bar_<treatment>.png")
