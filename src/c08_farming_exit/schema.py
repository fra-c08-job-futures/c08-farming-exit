"""
This is a script for definiing dataframe schemas for each csv table
"""

import pandera as pa

class CROP_PRODUCTION_2023_Dataframe(pa.DataFrameModel):
    interview__key: object = pa.Field(ge=0)
    column2: float = pa.Field(lt=10)
    column3: str = pa.Field(isin=[*"abc"])




class SchemaClass2(pa.DataFrameModel):
    interview__key: object = pa.Field(ge=0)
    column2: float = pa.Field(lt=10)
    column3: str = pa.Field(isin=[*"abc"])


class SchemaClass3(pa.DataFrameModel):
    interview__key: object = pa.Field(ge=0)
    column2: float = pa.Field(lt=10)
    column3: str = pa.Field(isin=[*"abc"])


