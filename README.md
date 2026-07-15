# Future Rural Africa - C08: Staying in or Leaving Farming
This repository uses the Z03 survey data from the University of Bonn's "Future Rural Africa" project to investigate who remains in or leaves farming.

The repo is structured as follows:

```
c08-farming-exit/
├── .venv/                      ← managed by uv
├── src/
│   └── c08_farming_exit/
│       ├── __init__.py
│       ├── config.py           ← paths, constants, parameters
│       ├── data_cleaning.py    ← cleaning functions/classes
│       ├── features.py         ← feature engineering
│       ├── visuals.py          ← plotting helpers
│       └── stata_utils.py      ← pystata init
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_modeling.ipynb
├── stata/
│   └── blabliblub.do           ← .do files live outside src (not Python)
├── data/
│   ├── raw/
│   └── processed/
├── pyproject.toml              ← library dependency management
├── uv.lock                     ← managed by uv
├── .gitignore                  ← files not sent to the remote on github.com
└── README.md
```