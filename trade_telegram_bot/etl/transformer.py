from datetime import datetime

import pandas as pd
from pandas.core.util.hashing import hash_pandas_object

from trade_telegram_bot.utils.consts import date_format_mapper, dtypes_mapper, name_cols_mapper, split_values_mapper


class Transformer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def modify(self) -> pd.DataFrame:
        self._rename_columns(name_cols_mapper)
        self._unify_date_format(date_format_mapper)
        self._distribution_values(split_values_mapper)
        self._hash_calc()
        self._change_dtypes()
        return self.df

    def _rename_columns(self, cols: dict[str, str]) -> None:
        self.df.rename(columns=cols, inplace=True)

    def _unify_date_format(self, mapper: dict[str, str]) -> None:
        for column, frmt in mapper.items():
            self.df[column] = self.df[[column]].apply(
                lambda x: datetime.strptime(x[0], frmt).replace(year=2023), axis=1
            )

    def _distribution_values(self, mapper: dict[str, dict[str, str]]) -> None:
        for column, values in mapper.items():
            self.df[values["cols"]] = self.df[column].str.split(values["delimiter"], expand=True)
            self._change_dtypes(dict(zip(values["cols"], values["dtypes"])))
            self.df.drop(column, axis=1, inplace=True)

    def _hash_calc(self) -> None:
        self.df["id"] = hash_pandas_object(self.df)

    def _change_dtypes(self, custom_mapper=dtypes_mapper):
        for col, dtype in custom_mapper.items():
            self.df[col] = self.df[col].astype(dtype)
