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