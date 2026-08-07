"""Feature engineering functions."""

import numpy as np 
import pandas as pd
from c08_farming_exit import config


def agricultural_wage_per_hour(df, country, payment_frequency, agriculture_only=False):
    """Calculates the median agricultural wage per hour for a given country and payment frequency.

    Parameters
    ----------
    df : pd.DataFrame
    country : str
    payment_frequency : str
        The payment frequency, either "Per month" or "Per day".
    agriculture_only : bool, optional
        Whether to consider only agriculture-related employment, by default False.

    Returns
    -------
    float
        The median agricultural wage per hour.
    """
    mask = (df["country"] == country) \
        & (df["wage_empl_seasonal_casual_payment_frequency"] == payment_frequency) \
        & (df["wage_empl_type"] == "Seasonal")

    if agriculture_only:
        mask &= df["sector_off_farm_empl_last_12_months"] == "agriculture"

    df = df.loc[mask].copy()

    if payment_frequency == "Per month":
        hours = df["wage_empl_seasonal_casual_hours_per_year"] / 12
    elif payment_frequency == "Per day":
        hours = df["wage_empl_seasonal_casual_duration_hours_per_day"]
    else:
        raise ValueError(f"payment_frequency '{payment_frequency}' not recognized. Use 'Per month' or 'Per day'.")

    wage_per_hour = df["wage_empl_seasonal_casual_wage_per_interval"] / hours.replace(0, np.nan)

    return wage_per_hour.median()

def compute_hourly_wage_for_casual_work(row):
    """Calculates the hourly wage for casual/seasonal work dependent on different payment frequencies.

    Parameters
    ----------
    df : pd.DataFrame
    country : str
    payment_frequency: str, e.g. "Per day", "Per month"
    agriculture_only: boolean
        Set to True if you only want to use the agricultural sector. 

    Returns
    -------
    Hourly wage, or np.nan if it cannot be computed (float).
    """

    wage = row["wage_empl_seasonal_casual_wage_per_interval"]
    freq = row["wage_empl_seasonal_casual_payment_frequency"]
    days_wk = row["wage_empl_seasonal_casual_duration_days_per_week"]
    hrs_day = row["wage_empl_seasonal_casual_duration_hours_per_day"]
    hpy = row["wage_empl_seasonal_casual_hours_per_year"]

    if pd.isna(wage):
        return np.nan

    if freq in ("Per year", "Lumpsum"):
        hours = hpy                         # <- reuse precomputed value directly
    elif pd.isna(days_wk) or pd.isna(hrs_day):
        return np.nan
    elif freq == "Per day":
        hours = hrs_day
    elif freq == "Per week":
        hours = days_wk * hrs_day
    elif freq == "Per fortnight":
        hours = days_wk * hrs_day * 2
    elif freq == "Per month":
        hours = days_wk * hrs_day * config.WEEKS_PER_MONTH
    elif freq == "Per quarter":
        hours = days_wk * hrs_day * config.WEEKS_PER_MONTH * 3
    elif freq == "Per half year":
        hours = days_wk * hrs_day * config.WEEKS_PER_MONTH * 6
    else:
        return np.nan

    return wage / hours if hours else np.nan

def count_ones(df, cols, new_col):
    """
    Count the number of 1s per row across a set of dummy (0/1) columns.

    NaNs are skipped if other valid values exist in the row; if all
    specified columns are NaN for a row, the result is NaN (not 0).

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe containing the dummy columns. Modified in place.
    cols : list of str
        Dummy-coded (0/1) columns to sum across.
    new_col : str, default 'count_ones'
        Name of the output column.

    Returns
    -------
    pandas.DataFrame
        df with `new_col` added.
    """
    df[new_col] = df[cols].sum(axis=1)
    df.loc[df[cols].isna().all(axis=1), new_col] = np.nan
    return df

def collapse_main_income_use(df, employment_types, spending_categories):
    """Collapsing main income usage information across employment types by selecting 
    if a spending category was listed as top 3.

    Parameters
    ----------
    df : pd.DataFrame
    employment_types : list of str, based on column name logic!
    spending_categories : list of str, based on column name logic!

    Returns
    -------
    pd.DataFrame
        df with 7 new "main_use_{category}_top_3" columns.
    """

    df = df.copy()
    #build list of input column names
    input_cols = [f"{p}_main_use_{c}" for p in employment_types for c in spending_categories]

    #check which rows how only NaNs
    all_nan = df[input_cols].isna().all(axis=1)

    # flag = 1 if ANY employment type has this category ranked 1, 2, or 3
    flags = pd.DataFrame({
        cat: df[[f"{p}_main_use_{cat}" for p in employment_types]]
                .isin([1, 2, 3])
                .any(axis=1)
                .astype(int)
        for cat in spending_categories
    })

    #apply all-nan mask
    flags[all_nan] = np.nan

    df[[f"main_use_{c}_top_3" for c in spending_categories]] = flags

    return df

def convert_currency(df, columns, country_col, rates):
    """
    Convert specified local-currency columns to another currency based on
    a provided mapping logic.

    Parameters
    ----------
    df : pd.DataFrame
    columns : list[str]
        Names of the columns (in local currency) to convert.
    country_col : str
    rates : dict
        Mapping of local-currency columns to another currency.

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()

    # Map country to rate; unmatched countries become NaN
    rate_series = df[country_col].map(rates)

    for col in columns:
        df[col] = df[col] * rate_series

    return df