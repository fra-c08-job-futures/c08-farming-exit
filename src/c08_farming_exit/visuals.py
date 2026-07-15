"""Reusable plotting helpers."""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

def plot_price_distribution(df, bins=15):
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(df["price"], bins=bins, edgecolor="white", color="steelblue")
    ax.set_xlabel("Price (USD)")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Car Prices")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    plt.tight_layout()
    plt.show()
    return fig, ax