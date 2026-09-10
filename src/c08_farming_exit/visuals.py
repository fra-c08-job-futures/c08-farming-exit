"""Reusable plotting helpers."""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd


def plot_stacked_bar(df, col, title, legend_title, filename):
    """
    Plot a stacked bar chart of each category's percentage share by country.
    Saves the figure to "output/{filename}".

    Parameters
    ----------
    df : pandas.DataFrame
        Data containing a "country" column and `col`.
    col : str
        Categorical column to compute shares for.
    title : str
        Plot title.
    legend_title : str
        Legend title.
    filename : str
        Output filename, relative to "output/".
    """
    countries = ["Botswana", "Namibia", "Kenya", "Tanzania", "Zambia"]

    counts = (
        df[df["country"].isin(countries)]
        .groupby(["country", col])
        .size()
        .unstack(col)
        .reindex(countries)
    )

    totals = counts.sum(axis=1)
    shares = counts.div(totals, axis=0) * 100  # convert to percentage shares

    ax = shares.plot(kind="bar", stacked=True, figsize=(10, 6))

    # Add percentage labels inside each stacked segment
    for container in ax.containers:
        labels = [f"{v:.1f}%" if v >= 3 else "" for v in container.datavalues]
        ax.bar_label(
            container,
            labels=labels,
            label_type="center",
            fontsize=8,
            color="white",
            weight="bold",
        )

    plt.xlabel("Country")
    plt.ylabel("Share (%)")
    plt.title(title)
    plt.legend(title=legend_title, bbox_to_anchor=(1.02, 1), loc="upper left")

    ax.set_xticklabels([f"{c}\n(n={int(totals[c])})" for c in countries], rotation=45)

    plt.tight_layout()
    # plt.savefig(f"../output/{filename}", dpi=150, bbox_inches="tight")
    # plt.show()
    plt.close()