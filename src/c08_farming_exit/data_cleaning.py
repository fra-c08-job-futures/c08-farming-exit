"""Data cleaning functions and classes."""

import pandas as pd
import numpy as np 
from pathlib import Path
from c08_farming_exit import features, mappings

# ============================================================
# STANDALONE DATA CLEANING TASKS
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
    mapping : dict
        Dict of {original_col_name: (new_name, dtype, fill_value)}

    Returns
    -------
    pd.DataFrame
    """
    for col, (_, dtype, fill_value, _) in feature_dict.items():
        
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

def fill_missings(df, feature_dict):
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
    for col, (_, _, fill_value, _) in feature_dict.items():
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

def mapping(df, category_col, mapping, new_col, field=None):
    """
    Map a category column through a dict to create/overwrite a new column.
    Works for simple and complex mappings.
    Simple (e.g. mappings.acres_conversion_factors): 
        Donnot provide 'field' and the value under the key is extracted. 
    Complex (e.g. mappings.education_mapping): 
        The mapping values are expected to be dicts. 
        Set 'field' to the key of interest and the value stored under that key is extracted.
    
    Parameters
    ----------
    df : pd.DataFrame
    category_col : str
        Column containing the mapping categories.
    mapping: dict
        Mapping stating the mapping rules.
    new_col: str
        Columns name for the mapped output column.
    filed : str
        Only to be filled for complex mappings (see above)
    suffix: str

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy() 
    lookup = (lambda k: mapping.get(k, {}).get(field)) if field else mapping.get
    df[new_col] = df[category_col].map(lookup)
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

# ============================================================
# WRAPPER DATA CLEANING TASKS
# ============================================================

def load_and_preprocess(base_path, filename, feature_dict):
    """Load a CSV, then select, cast, fill, and rename columns. 

    Thin wrapper around `load_csv()`, `fill_missings()`, 
    and `enforce_dtypes()`.
    
    Parameters
    ----------
    base_path : str
        Path to the raw data directory.
    filename : str
        Name of the CSV file, e.g. "Zambia_expenditure_on_crops.csv".
    feature_dict : dict
        Dict of {original_col_name: (new_name, dtype, fill_value, mapping)}.

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
    #Take care of missings
    df = fill_missings(df, available)
    #Rename
    rename_map = {k: v[0] for k, v in available.items() if k != v[0]}
    df = df.rename(columns=rename_map)

    return df

def create_education_features(df, category_col='education_level', edu_mapping=mappings.education_mapping):
    """
    Clean 'education_level' and add a 'years_of_schooling' column.

    Thin wrapper around `mapping()` that applies the education mapping twice:
    once to derive years of schooling, once to clean the education_level labels.

    Parameters
    ----------
    df : pd.DataFrame
    category_col : str, default 'education_level'
        Column containing the raw education categories.
    edu_mapping : dict, optional
        Complex mapping dict (see `mapping()` docstring) with per-category
        'years_of_schooling' and 'education_level' keys.

    Returns
    -------
    pd.DataFrame
    """
    df = mapping(df, category_col, edu_mapping, 'years_of_schooling', field='years_of_schooling')
    df = mapping(df, category_col, edu_mapping, category_col,         field=category_col)

    return df

def convert_land_sizes_to_acres(df, country, measurement_col, acres_conversion_factors):
    """
    Converts all land_size_ columns in df to acres, based on the per-row unit given in `measurement_col`.
    
    Conversion factors are added to the df with `mapping()`, 
    Conversion factors are applied to the respective columns with `apply_factor()`.

    Parameters
    ----------
    df : pd.DataFrame
    measurement_col : str

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    #Define which columns need to be converted
    land_size_cols = [c for c in df.columns if c.startswith('land_size_')]

    #Dropping NaN rows
    n_before = len(df)
    df = df.dropna(subset=['land_measurement'])
    n_dropped = n_before - len(df)
    if n_dropped > 0:
        print(f"convert_land_sizes_to_acres: {country} - Dropped {n_dropped} rows with NaN in 'land_measurement'")

    #Overwrite any "Other.." with "Lima"
    df[measurement_col] = np.where(df[measurement_col].str.startswith('Other'), 'Lima', df[measurement_col])

    #Add the acres conversion factors
    df =  mapping(df, measurement_col, acres_conversion_factors, "factor", field=None)
    #Apply the conversion factors
    df = apply_factor(df, "factor", land_size_cols, "")

    # Overwrite all non-NaN measurement labels to 'Acres'
    df[measurement_col] = np.where(df[measurement_col].notna(), 'Acres', df[measurement_col])

    return df

def crop_production_manual_cleaning(df, key_col):
    """
    Collapses crop production data to one row per household by deleting the dimension of crop types.    
    This is a manual function that cannot be reused for any other table.
    
    Sales revenues are calculated using `calculate_revenue()`, 
    
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
    df[["crop_home_consumption"]] = (
        df[["crop_home_consumption_amount"]] != 0
    ).groupby(df[key_col]).transform("any").astype(int)
    df = df.drop(columns=["crop_home_consumption_amount"])

    #Calculate the total sale revenues of crop production per hh (in local currency)
    df = calculate_revenue(df, "crop_sale_amount", "crop_sale_price_per_unit", "crop_sale_revenue")
    df["crop_sale_revenue"] = df.groupby("interview_key")["crop_sale_revenue"].transform("sum")

    return df.drop_duplicates(subset=key_col).reset_index(drop=True)

def create_livestock_features(df, category_col='livestock_type', conversion_factors=mappings.livestock_conversion_factors):
    """
    Clean livestock ownership data and collapse to one row per household.

    Thin wrapper around `mapping()`, `apply_factor()`, `calculate_revenue()`,
    and `aggregate_by_hh()` that converts livestock counts to TLU, computes
    sale revenue, and aggregates across animal types to the household level.

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

    df = mapping(df, category_col, conversion_factors, "factor", field=None)
    df = apply_factor(df, "factor", number_cols, "tlu")
    df = calculate_revenue(df, "livestock_number_sold", "livestock_price_head_sold", "livestock_revenue_sold")
    df = aggregate_by_hh(df, [category_col])

    return df

def create_asset_features(df, category_col='asset_type'):
    """
    Clean assets owned data and collapse to one row per household.

    Thin wrapper around `calculate_revenue()` and `aggregate_by_hh()` that
    computes the value of owned assets and aggregates across asset types
    to the household level.

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
    df = aggregate_by_hh(df, [category_col])

    return df

def create_other_income_features(df, frequency_col='other_income_frequency', source_col='other_income_source', frequency_mapping=mappings.income_frequency):
    """
    Clean other income data and collapse to one row per household.

    Filters out rows with an unrecognized income frequency, annualizes
    the income amount using `mapping()` and `apply_factor()`, then
    aggregates across income sources/frequencies to the household level.

    Parameters
    ----------
    df : pd.DataFrame
    frequency_col : str, default 'other_income_frequency'
        Column containing the income frequency categories (e.g. weekly,
        monthly, yearly), used to look up the annualization factor.
    source_col : str, default 'other_income_source'
        Column identifying the income source; dropped during aggregation
        along with `frequency_col`.
    frequency_mapping : dict, optional
        Mapping of frequency label -> annualization factor.

    Returns
    -------
    pd.DataFrame
    """
    df = df[df[frequency_col].isin(frequency_mapping.keys())]
    df = mapping(df, frequency_col, frequency_mapping, "factor", field=None)
    df = apply_factor(df, "factor", ["other_income_amount"], "yearly")
    df = aggregate_by_hh(df, [source_col, frequency_col])

    return df

# ============================================================
# EDA STUFF
# ============================================================

def most_common_or_nan(x):
    counts = x.value_counts()
    if counts.empty:
        return pd.NA
    return counts.idxmax()