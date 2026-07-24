"""
Für jeden Table definiere hier transformationsfunktion, welche aus raw CSV den transformed polars dataframe macht, mit dem du arbeiten willst.

"""


from c08_farming_exit import config
from c08_farming_exit.data_cleaning import fill_missings


function_list = [
    transform_CROP_PRODUCTION_2023,
    transform_CROP_PRODUCTION_2024,
]


def transform_CROP_PRODUCTION_2023() -> pandas.DataFrame:
    df = pandas.read_csv(config.CROP_PRODUCTION_2023_PATH)
    df = fill_missings(df, xxx)


    ...

    return df

def transform_CROP_PRODUCTION_2024() -> pandas.DataFrame:
    pass

