"""Data cleaning functions and classes."""

import pandas as pd
from pathlib import Path
from c08_farming_exit import features


def load(base_path, filename, col_rename):
    """Load CSV, selecting and renaming columns in one step.
    Returns none in case the CSV is not existing. """

    path = base_path / filename
    if not path.exists():
        print(f"[{filename}] File not found: {path}")
        return None
    else:
        df = pd.read_csv(base_path / filename)

        available = {k: v for k, v in col_rename.items() if k in df.columns}
        missing = [k for k in col_rename if k not in df.columns]

        if missing:
            print(f"[{filename}] Missing columns: {missing}")

        return df[list(available.keys())].rename(columns={k: v for k, v in available.items() if k != v})
    

def most_common_or_nan(x):
    counts = x.value_counts()
    if counts.empty:
        return pd.NA
    return counts.idxmax()