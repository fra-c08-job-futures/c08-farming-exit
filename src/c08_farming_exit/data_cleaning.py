"""Data cleaning functions and classes."""

import pandas as pd
import numpy as np 
from pathlib import Path
from c08_farming_exit import features, mappings

# ============================================================
# GENERAL DATA CLEANING TASKS
# ============================================================

def load_and_preprocess(base_path, filename, mapping):
    """Load a CSV, then select, cast, fill, and rename columns. 

    All steps are performed according to `mapping`. Missing values are
    filled using `fill_missings()`, and casting is enforced using
    `enforce_dtypes()`.
    
    Parameters
    ----------
    base_path : str
        Path to the raw data directory.
    filename : str
        Name of the CSV file, e.g. "Zambia_expenditure_on_crops.csv".
    mapping : dict
        Dict of {original_col_name: (new_name, dtype, fill_value)}.

    Returns
    -------
    pd.DataFrame
        The processed dataframe, or None if the CSV does not exist.
    """
    path = base_path / filename

    #Check if file exists
    if not path.exists():
        print(f"[{filename}] File not found: {path}")
        return None

    df = pd.read_csv(path)

    #Check if all columns listed in mapping exist
    available = {k: v for k, v in mapping.items() if k in df.columns}
    missing = [k for k in mapping if k not in df.columns]
    if missing:
        print(f"[{filename}] Missing columns: {missing}")

    #Select columns
    df = df[list(available.keys())]
    #Define datatypes
    df = enforce_dtypes(df, available)
    #Take care of missings
    df = fill_missings(df, available)
    #Rename
    rename_map = {k: v[0] for k, v in available.items() if k != v[0]}
    df = df.rename(columns=rename_map)

    return df

def enforce_dtypes(df, mapping):
    """
    Casts each column in df to the dtype specified in mapping.

    Parameters
    ----------
    df : pd.DataFrame
    mapping : dict
        Dict of {original_col_name: (new_name, dtype, fill_value)}

    Returns
    -------
    pd.DataFrame
    """
    for col, (_, dtype, fill_value) in mapping.items():
        
        #Before enforcing dtypes we need 2 pre-processing steps
        #1. yes/no features need to be converted into 1/0 
        if isinstance(fill_value, str) and fill_value.startswith("dummy"):
            df[col] = df[col].map({'Yes': 1.0, 'No': 0.0})
        #2. Stata extended missing-value codes (., .a, .b, ... .z) exist, so we need to enforce numeric conversion 
        if isinstance(dtype, str) and dtype.startswith("float"):
            df[col] = pd.to_numeric(df[col], errors="coerce")

        if col in df.columns:
            df[col] = df[col].astype(dtype)

    return df

def fill_missings(df, mapping):
    """
    Fills missing values in df's columns based on mapping.

    Parameters
    ----------
    df : pd.DataFrame
    mapping : dict
        Dict of {original_col_name: (new_name, dtype, fill_value)}.
        fill_value can be None (skip), 0 (or any literal), "mean",
        "median", or "missing".

    Returns
    -------
    pd.DataFrame
    """
    for col, (_, _, fill_value) in mapping.items():
        if fill_value is None:
            continue
        if fill_value == "mean":
            df[col] = df[col].fillna(df[col].mean())
        elif fill_value == "median":
            df[col] = df[col].fillna(df[col].median())
        elif fill_value == "missing":
            df[col] = df[col].fillna("missing")
        elif fill_value == "dummy":
            df[col] = df[col].fillna(0.0)
        else:
            df[col] = df[col].fillna(fill_value)

    return df
            
# ============================================================
# SPECIFIC DATA CLEANING TASKS
# ============================================================

def most_common_or_nan(x):
    counts = x.value_counts()
    if counts.empty:
        return pd.NA
    return counts.idxmax()

def add_years_of_schooling(df, education_mapping):
    """
    Clean 'education_level' and add a 'years_of_schooling' column based on
    a mapping dictionary.

    Parameters
    ----------
    df_database : pd.DataFrame
    education_mapping : dict

    Returns
    -------
    pd.DataFrame
    """
    df['years_of_schooling'] = df['education_level'].map(
        lambda x: mappings.education_mapping.get(x, {}).get('years_of_schooling')
    )

    df['education_level'] = df['education_level'].map(
        lambda x: mappings.education_mapping.get(x, {}).get('education_level')
    )

    return df

def convert_land_sizes_to_acres(df, country, measurement_col, acres_conversion_factors):
    """
    Converts all land_size_ columns in df to acres, based on the per-row unit given in `measurement_col`.

    Parameters
    ----------
    df : pd.DataFrame
    measurement_col : str

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    land_size_cols = [c for c in df.columns if c.startswith('land_size_')]

    #Dropping NaN rows
    n_before = len(df)
    df = df.dropna(subset=['land_measurement'])
    n_dropped = n_before - len(df)
    if n_dropped > 0:
        print(f"convert_land_sizes_to_acres: {country} - Dropped {n_dropped} rows with NaN in 'land_measurement'")

    #Overwrite any "Other.." with "Lima"
    df[measurement_col] = np.where(df[measurement_col].str.startswith('Other'), 'Lima', df[measurement_col])

    #Create pandas series: one value per row containing the factor
    factors = df[measurement_col].map(acres_conversion_factors)

    for col in land_size_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce') * factors

    # Overwrite all non-NaN measurement labels to 'Acres'
    df[measurement_col] = np.where(df[measurement_col].notna(), 'Acres', df[measurement_col])

    return df

def resolve_duplicates(df, key_col, sort_col=None, ascending=True):
    """
    Resolve duplicate rows in key_col by sorting and keeping the first
    row per key.
    Only use this function when there are very little duplicates and you
    know what you are doing!

    Parameters
    ----------
    df : pd.DataFrame
    key_col : str
        Rows sharing the same value here are considered duplicates.
    sort_col : str
        Secondary column used to decide which duplicate to keep
    ascending : bool or list of bool
        Sort order.

    Returns
    -------
    pd.DataFrame
    """
    sorted_df = df.sort_values(by=[key_col, sort_col], ascending=ascending)
    return sorted_df.drop_duplicates(subset=key_col, keep="first")

def add_missing_indicators(df, columns, sentinel=99999, suffix='_missing'):
    """
    Add a binary indicator column for each given column, flagging rows
    that are missing. 
    Only use this after filling missing values with a sentinel=99999!

    Parameters
    ----------
    df : pd.DataFrame
    columns : list of str
        Columns to check for the sentinel value.
    sentinel : int or float
        Placeholder value used for missing data, set to 99999.
    suffix : str
        Suffix appended to column name for the new indicator column.

    Returns
    -------
    pd.DataFrame
    """
    for col in columns:
        df[f"{col}{suffix}"] = (df[col] == sentinel).astype(int)
    return df

def crop_production_manual_cleaning(df, key_col):
    """
    Collapses crop production data to one row per household by deleting the dimension of crop types.    
    This is a manual function that cannot be reused for any other table. 
    
    Parameters
    ----------
    df : pd.DataFrame
    key_col : str
        Column to group by and collapse to one row per key.
    exchange_rates : dict

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
                      "crop_tractor"]
    df[reduction_list] = df.groupby(key_col)[reduction_list].transform('max')

    #If there is home consumption for any crop, set 1 for the entire household
    df[["crop_home_consumption_amount"]] = (
        df[["crop_home_consumption_amount"]] != 0
    ).groupby(df[key_col]).transform("any").astype(int)

    #Calculate the total sale revenues of crop production per hh (in local currency)
    df["crop_sale_revenue"] = df["crop_sale_amount"] * df["crop_sale_price_per_unit"]
    df["crop_sale_revenue_total"] = df.groupby("interview_key")["crop_sale_revenue"].transform("sum")
    df = df.drop(columns=["crop_sale_amount", "crop_sale_price_per_unit", "crop_sale_revenue"])

    return df.drop_duplicates(subset=key_col).reset_index(drop=True)

def conversion(df, type_col, number_cols, conversion_factors, suffix):
    """
    Conversion of a column based on the conversion_factor mapping. 

    Parameters
    ----------
    df : pd.DataFrame
    type_col : str
        Column name indicating the categories used for conversion.
    number_col : list of str
        Column name(s) with numeric value to be converted.
    conversion_factors : dict
        Mapping stating the conversion categories and the respective conversion factors. 
    suffix: str

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    factor = df[type_col].map(conversion_factors)

    for col in number_cols:
        df[f"{col}_{suffix}"] = df[col] * factor

    df = df.drop(columns=number_cols)

    return df

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
    Groups a DataFrame by 'country' and 'interview_key', summing all
    other numeric columns (collapsing across 'dimension_col' categories).
    
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

    result = df.groupby(["interview_key"], as_index=False).sum()

    return result
