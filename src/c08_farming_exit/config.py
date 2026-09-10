"""Central place for parameters that may change: paths, constants, settings."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
STATA_DIR = PROJECT_ROOT / "stata"

STATA_EDITION = "se" # "se" = Stata SE | "mp" = Stata/MP | "be" = Stata/BE
STATA_PATH = r"C:\Program Files\Stata18\utilities" # path to Stata's "utilities" folder, adjust per machine

WEEKS_PER_MONTH = 4.345  # 52/12