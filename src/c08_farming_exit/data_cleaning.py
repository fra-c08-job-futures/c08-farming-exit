"""Data cleaning functions."""

import pandas as pd
import numpy as np 
from pathlib import Path
from c08_farming_exit import features, mappings

# ============================================================
# STANDALONE DATA CLEANING FUNCTION
# ============================================================

def load_csv(base_path, filename):
    """Loads a CSV from a predefined path.
    
    Parameters
    ----------
    base_path : str
        Path to the raw data directory.
    filename : str
        Name of the CSV file, e.g. "Zambia_expenditure_on_crops.csv".

    Returns
    -------
    pd.DataFrame
    """
    path = base_path / filename

    #Check if file exists
    if not path.exists():
        print(f"[{filename}] File not found: {path}")
        return None

    return pd.read_csv(path)

def enforce_dtypes(df, feature_dict):
    """
    Casts each column in df to the dtype specified in mapping.

    Parameters
    ----------
    df : pd.DataFrame
    feature_dict : dict
        Dict of {original_col_name: (new_name, dtype, dummy, mapping)}

    Returns
    -------
    pd.DataFrame
    """
    for col, (_, dtype, dummy, _) in feature_dict.items():
        
        #Before enforcing dtypes we need 2 pre-processing steps
        #1. yes/no features need to be converted into 1/0 
        if isinstance(dummy, str) and dummy.startswith("dummy"):
            df[col] = df[col].map({'Yes': 1.0, 'No': 0.0})
        #2. Stata extended missing-value codes (., .a, .b, ... .z) exist, so we need to enforce numeric conversion 
        if isinstance(dtype, str) and dtype.startswith("float"):
            df[col] = pd.to_numeric(df[col], errors="coerce")

        if col in df.columns:
            df[col] = df[col].astype(dtype)

    return df

def mapping(df, feature_dict):
    """
    Apply value mappings defined in feature_dict to create/overwrite columns.

    Parameters
    ----------
    df : pd.DataFrame
    feature_dict : dict
        Dict of {source_col: (new_col, dtype, default, value_map)}.

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()

    for col, (_, _, _, value_map) in feature_dict.items():
        if value_map is not None:
            df[col] = df[col].map(value_map)

    return df

def apply_factor(df, factor_col, number_cols, suffix):
    """
    Conversion of a column based on a factor. 

    Parameters
    ----------
    df : pd.DataFrame
    factor_col : str
        Column containing the conversion factors.
    number_cols : list of str
        Columns to which the conversion should be applied, must be numeric.
    suffix: str

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    for col in number_cols:
        df[f"{col}_{suffix}"] = df[col] * df[factor_col]
    return df.drop(columns=number_cols + [factor_col])

def calculate_revenue(df, number_col, price_col, new_col_name):
    """
    Calculate the revenue of a sold product (e.g. crop/animal)

    Parameters
    ----------
    df : pd.DataFrame
    number_col : int
    price_col : int
    new_col_name: str
        name of new column, e.g. livestock_revenue_sold/crop_revenue_sold

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    df[new_col_name] = df[number_col] * df[price_col]
    df = df.drop(columns=[number_col, price_col])

    return df

def aggregate_by_hh(df, dimension_col):
    """
    Groups a DataFrame by 'interview_key', summing all other numeric 
    columns (collapsing across 'dimension_col' categories).
    
    Parameters
    ----------
    df : pd.DataFrame
        containing various rows per hh
    dimension_col: list
        dimension columns to be dropped when collapsing

    Returns
    -------
    pd.DataFrame
        only containing one row per hh
    """
    df = df.drop(columns=dimension_col, errors="ignore")

    #makes sure that a hh with all NaNs will aggreagate to NaNs also
    result = df.groupby(["interview_key"], as_index=False).sum(min_count=1)

    return result

def resolve_duplicates(df, key_col, sort_col=None, ascending=True):
    """
    Resolve duplicate rows in key_col by sorting and keeping the first
    row per key.
    Only use this function when there are very little duplicates and you
    know what you are doing!

    Parameters
    ----------
    df : pd.DataFrame
    key_col : str or list of str
        Rows sharing the same value(s) here are considered duplicates.
    sort_col : str
        Secondary column used to decide which duplicate to keep
    ascending : bool or list of bool
        Sort order.

    Returns
    -------
    pd.DataFrame
    """
    key_cols = [key_col] if isinstance(key_col, str) else list(key_col)
    sorted_df = df.sort_values(by=key_cols + [sort_col], ascending=ascending)
    return sorted_df.drop_duplicates(subset=key_cols, keep="first")

def make_pivot_table(df, category_columns, index,  aggfunc='size', values=None):
    """
    Pivot a long-format dataframe into a wide-format pivot table.
    #TODO: Watch out! Pandas silently drops NaN rows. 

    Parameters
    ----------
    df : pd.DataFrame (long format)
    category_columns : str
        Column to spread into new columns. 
    index : str or list of str
        e.g. "interview_key" or "personal_id"
    aggfunc : str or callable, default 'count'
        e.g. 'sum', 'mean', 'first'. Only used when `values` is provided.
    values : str, optional
        Column with category-specific values. If None, categorical dummies are created. 

    Returns
    -------
    pd.DataFrame (wide-format dataframe)
        
    Examples
    --------
    >>> df = pd.DataFrame({
    ...     'id': [1, 1, 2, 2],
    ...     'category': ['A', np.nan, 'A', 'B'],
    ...     'amount': [10, 20, 5, 15]
    ... })
    >>> make_pivot_table(df, index='id', category_columns='category') #if only interested in categorical dummies
    >>> make_pivot_table(df, index='id', category_columns='category', aggfunc='sum', values='amount') #if interested in category-specific values
    """
    df = df.copy()
 
    if values is None:
        pivoted = pd.pivot_table(
            df,
            index=index,
            columns=category_columns,
            aggfunc='size'
        )
        pivoted = (pivoted > 0).astype(int)
    else:
        pivoted = pd.pivot_table(
            df,
            index=index,
            columns=category_columns,
            values=values,
            aggfunc=aggfunc
        )

    pivoted.columns = [f"{category_columns}_{col}" for col in pivoted.columns]
    pivoted.columns.name = None  # remove leftover columns-index label
    
    return pivoted.reset_index()

def flag_group_if_any_true(df, key_col, flag_cols):
    """
    For each column in flag_cols, if any row within a group (grouped by
    key_col) has a truthy value (non-zero/True), set that value to 1 
    for all rows in that group; otherwise 0.

    Parameters
    ----------
    df : pandas.DataFrame
    key_col : str or list
        The name of the column to group by.
    flag_cols : list of str
        List of column names containing binary/boolean flag values.

    Returns
    -------
    pandas.DataFrame
    """
    df[flag_cols] = df.groupby(key_col)[flag_cols].transform(lambda x: int(x.any()))
    return df

def group_by_and_average(df, key_col, avg_cols):
    """
    For each column in avg_cols, calculate the mean per key_col.

    Parameters
    ----------
    df : pandas.DataFrame
    key_col : str or list
        The name of the column to group by.
    avg_cols : list of str
        List of column names containing integers to be averaged.

    Returns
    -------
    pandas.DataFrame
    """
    df = df.groupby(key_col)[avg_cols].mean().reset_index()
    return df

# ============================================================
# WRAPPER DATA CLEANING FUNCTIONS
# ============================================================

def load_and_preprocess(base_path, filename, feature_dict):
    """Load a CSV, then select, cast, and rename columns. 

    Thin wrapper around `load_csv()`, and `enforce_dtypes()`.
    
    Parameters
    ----------
    base_path : str
        Path to the raw data directory.
    filename : str
        Name of the CSV file, e.g. "Zambia_expenditure_on_crops.csv".
    feature_dict : dict
        Dict of {original_col_name: (new_name, dtype, dummy, mapping)}.

    Returns
    -------
    pd.DataFrame
        The processed dataframe, or None if the CSV does not exist.
    """
    df = load_csv(base_path, filename)

    #Check if all columns listed in feature_dict exist
    available = {k: v for k, v in feature_dict.items() if k in df.columns}
    missing = [k for k in feature_dict if k not in df.columns]
    if missing:
        print(f"[{filename}] Missing columns: {missing}")

    #Select columns
    df = df[list(available.keys())]
    #Define datatypes
    df = enforce_dtypes(df, available)
    #Apply mapping 
    df = mapping(df, available)
    #Rename
    rename_map = {k: v[0] for k, v in available.items() if k != v[0]}
    df = df.rename(columns=rename_map)

    return df

def convert_land_sizes_to_acres(df, country):
    """
    Converts all land_size_ columns in df to acres, based on the per-row unit given in `measurement_col`.
    Conversion factors are applied to the respective columns with `apply_factor()`.

    Parameters
    ----------
    df : pd.DataFrame
    country : str
        Only used for print message

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    #Define which columns need to be converted
    land_size_cols = [c for c in df.columns if c.startswith('land_size_')]

    #Dropping NaN rows
    n_before = len(df)
    df = df.dropna(subset=["land_measurement"])
    n_dropped = n_before - len(df)
    if n_dropped > 0:
        print(f"convert_land_sizes_to_acres: {country} - Dropped {n_dropped} rows with NaN in 'land_measurement'")

    #Apply the conversion factors
    df = apply_factor(df, "land_measurement", land_size_cols, "acres")

    return df

def create_crop_production_features(df, key_col="interview_key"):
    """
    Collapses crop production data to one row per household by deleting the dimension of crop types.    
    This is a manual function that cannot be reused for any other table.
    
    True values in a group are identified using `flag_group_if_any_true()`.
    Sales revenues are calculated using `calculate_revenue()`.
    
    Parameters
    ----------
    df : pd.DataFrame
    key_col : str
        Column to group by and collapse to one row per key.

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()

    #If there is a true value for any crop, set 1 for the entire household
    reduction_list = ["crop_harvested", 
                      "crop_sale", 
                      "crop_storage", 
                      "crop_buyer_market", 
                      "crop_buyer_trader", 
                      "crop_buyer_cooperative", 
                      "crop_buyer_commercial_farm", 
                      "crop_buyer_hospitality", 
                      "crop_buyer_government", 
                      "crop_organic_fertilizer", 
                      "crop_inorganic_fertilizer", 
                      "crop_pesticides", 
                      "crop_tractor",
                      "crop_home_consumption_amount"]
    df = flag_group_if_any_true(df, key_col, reduction_list)
    df = df.rename(columns={'crop_home_consumption_amount': 'crop_home_consumption'})

    #Calculate the total sale revenues of crop production per hh (in local currency)
    df = calculate_revenue(df, "crop_sale_amount", "crop_sale_price_per_unit", "crop_sale_revenue")
    df["crop_sale_revenue"] = df.groupby("interview_key")["crop_sale_revenue"].transform("sum")

    #Calculcate unique crop types per hh
    df["crop_type_diversity"] = df.groupby("interview_key")["crop_type"].transform("nunique")
    df = df.drop(columns=["crop_type"])

    return df.drop_duplicates(subset=key_col).reset_index(drop=True)

def create_livestock_features(df, category_col='livestock_type'):
    """
    Clean livestock ownership data and collapse to one row per household.

    Thin wrapper around `apply_factor()`, `calculate_revenue()`,
    and `aggregate_by_hh()` that converts livestock counts to TLU, computes
    sale revenue, adds livestock diversity and aggregates across animal types 
    to the household level.

    Parameters
    ----------
    df : pd.DataFrame
    category_col : str, default 'livestock_type'
        Column containing the animal type categories.
    conversion_factors : dict, optional
        Mapping of livestock_type -> TLU conversion factor.

    Returns
    -------
    pd.DataFrame
    """
    number_cols = ["livestock_number_owned", "livestock_number_lost_disease_theft", "livestock_number_lost_wildlife_attack"]

    df = apply_factor(df, "livestock_type", number_cols, "tlu")
    df = calculate_revenue(df, "livestock_number_sold", "livestock_price_head_sold", "livestock_revenue_sold")
    df["livestock_diversity"] = 1
    df = aggregate_by_hh(df, [category_col])

    return df

def create_asset_features(df, category_col='asset_type'):
    """
    Clean assets owned data and collapse to one row per household.

    Thin wrapper around `calculate_revenue()` and `aggregate_by_hh()` that
    computes the value of owned assets, adds asset diversity and aggregates 
    across asset types to the household level.

    Parameters
    ----------
    df : pd.DataFrame
    category_col : str, default 'asset_type'
        Column containing the asset type categories, dropped during
        aggregation.

    Returns
    -------
    pd.DataFrame
    """
    df = calculate_revenue(df, "asset_number_owned", "asset_price_per_unit", "asset_value")
    df["asset_diversity"] = 1
    df = aggregate_by_hh(df, [category_col])

    return df

def create_other_income_features(df, country, frequency_col='other_income_frequency', source_col='other_income_source'):
    """
    Clean other income data and collapse to one row per household.

    Filters out rows with an unrecognized income frequency, annualizes
    the income amount using `apply_factor()`, then aggregates across 
    income sources/frequencies to the household level using `aggregate_by_hh()`.

    Parameters
    ----------
    df : pd.DataFrame
    country: str
        Just used for printing message. 
    frequency_col : str, default 'other_income_frequency'
        Column containing the income frequency categories (e.g. weekly,
        monthly, yearly), used to look up the annualization factor.
    source_col : str, default 'other_income_source'
        Column identifying the income source; dropped during aggregation
        along with `frequency_col`.

    Returns
    -------
    pd.DataFrame
    """

    #Dropping NaN rows
    n_before = len(df)
    df = df.dropna(subset=[frequency_col])
    n_dropped = n_before - len(df)
    if n_dropped > 0:
        print(f"create_other_income_features: {country} - Dropped {n_dropped} rows with NaN in '{frequency_col}'")

    df = apply_factor(df, frequency_col, ["other_income_amount"], "monthly")
    df = aggregate_by_hh(df, [source_col, frequency_col])

    return df

def create_shock_features(df, category_col="shock_type_affected_last_12_months", index="interview_key"):
    """
    Map a category column through a dict, then pivot the result into a wide-format dataframe. 
    Combines `mapping()` + `make_pivot_table()`.

    Parameters
    ----------
    df : pd.DataFrame
    category_col : str
        Column containing the raw categories to be mapped.
    index : str or list of str
        Grouping key(s) for the pivot, e.g. "interview_key".


    Returns
    -------
    pd.DataFrame (wide-format dataframe)

    """

    #
    # df = mapping(df, country, category_col=category_col, mapping=mapping_dict, new_col=category_col)
    df = make_pivot_table(df, index=index, category_columns=category_col)
    return df

def create_coping_features(df, likelihood_col="shock_future_likelihood_change_income_source", key_col="interview_key"):
    """
    Create coping features out of the shocks_and_coping dataframe. 

    Uses `mapping()` + `flag_group_if_any_true()`.
  
    Parameters
    ----------
    df : pd.DataFrame
    likelihood_col : str
        Name of the column to map and include in the flag columns.
    key_col : str
        Column to group by for flagging (default "interview_key").

    Returns
    -------
    pd.DataFrame
    """

    # Flag a group as 1 if any is true
    cols = [c for c in df.columns if c.startswith("shock_coping")] + [likelihood_col]
    df = flag_group_if_any_true(df, key_col, cols)
    df = df[[key_col] + cols]

    return df.drop_duplicates(subset=key_col).reset_index(drop=True)

def create_off_farm_employment_features(df):
    """
    Clean off-farm employment data by resolving duplicate member-level
    records and flagging shared household-level attributes.

    Thin wrapper around `resolve_duplicates()` and `flag_group_if_any_true()`.
    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    key_col = ["interview_key", "members_id"]

    df = resolve_duplicates(df, key_col=key_col, sort_col="empl_type", ascending=True)

    #Create a dummy out of all "main_use" columns
    flag_cols = [c for c in df.columns if "main_use" in c]
    df = flag_group_if_any_true(df, key_col=key_col, flag_cols=flag_cols)

    return df

def create_time_allocation_features(df):
    """
    Clean time allocation data by calculating the share of a primary activity
    in a 24 hours day of a person. 

    Thin wrapper around `make_pivot_table()` and `group_by_and_average()`.
    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    df = make_pivot_table(df, index=["interview_key", "members_id", "time_slot"], category_columns="primary_activity")

    avg_cols = [c for c in df.columns if c.startswith('primary_activity_')]
    df = group_by_and_average(df, ['interview_key', 'members_id'], avg_cols)

    return df

# ============================================================
# EDA STUFF
# ============================================================

def most_common_or_nan(x):
    counts = x.value_counts()
    if counts.empty:
        return pd.NA
    return counts.idxmax()


# def fill_missings(df, feature_dict):
#     """
#     Fills missing values in df's columns based on mapping.

#     Parameters
#     ----------
#     df : pd.DataFrame
#     mapping : dict
#         Dict of {original_col_name: (new_name, dtype, fill_value)}.
#         fill_value can be None (skip), 0 (or any literal), "mean",
#         "median", or "missing".

#     Returns
#     -------
#     pd.DataFrame
#     """
#     for col, (_, _, fill_value, _) in feature_dict.items():
#         if fill_value is None:
#             continue
#         if fill_value == "mean":
#             df[col] = df[col].fillna(df[col].mean())
#         elif fill_value == "median":
#             df[col] = df[col].fillna(df[col].median())
#         elif fill_value == "missing":
#             df[col] = df[col].fillna("missing")
#         elif fill_value == "dummy":
#             df[col] = df[col].fillna(0.0)
#         else:
#             df[col] = df[col].fillna(fill_value)

#     return df



# def add_missing_indicators(df, columns, sentinel=99999, suffix='_missing'):
#     """
#     Add a binary indicator column for each given column, flagging rows
#     that are missing. 
#     Only use this after filling missing values with a sentinel=99999!

#     Parameters
#     ----------
#     df : pd.DataFrame
#     columns : list of str
#         Columns to check for the sentinel value.
#     sentinel : int or float
#         Placeholder value used for missing data, set to 99999.
#     suffix : str
#         Suffix appended to column name for the new indicator column.

#     Returns
#     -------
#     pd.DataFrame
#     """
#     for col in columns:
#         df[f"{col}{suffix}"] = (df[col] == sentinel).astype(int)
#     return df