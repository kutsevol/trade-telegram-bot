from datetime import datetime

import pandas as pd
from pandas.core.util.hashing import hash_pandas_object

from trade_telegram_bot.utils.consts import date_format_mapper, dtypes_mapper, name_cols_mapper, split_values_mapper


class Transformer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def modify(self) -> pd.DataFrame:
        """
        The function takes a dataframe, renames columns, unifies date formats, splits values, hashes
        values, and changes data types
        :return: The modified dataframe.
        """
        self._rename_columns(name_cols_mapper)
        self._unify_date_format(date_format_mapper)
        self._distribution_values(split_values_mapper)
        self._hash_calc()
        self._change_dtypes()
        return self.df

    def _rename_columns(self, cols: dict[str, str]) -> None:
        """
        It renames the columns of the dataframe

        :param cols: a dictionary of column names to rename. The keys are the old names, and the values are
        the new names
        :type cols: dict[str, str]
        """
        self.df.rename(columns=cols, inplace=True)

    def _unify_date_format(self, mapper: dict[str, str]) -> None:
        """
        It takes a dictionary of column names and date formats, and converts the date format of each column
        to the format specified in the dictionary

        :param mapper: a dictionary of column names and their corresponding date formats
        :type mapper: dict[str, str]
        """
        for column, frmt in mapper.items():
            self.df[column] = self.df[[column]].apply(
                lambda x: datetime.strptime(x[0], frmt).replace(year=2023), axis=1
            )

    def _distribution_values(self, mapper: dict[str, dict[str, str]]) -> None:
        """
        It takes a dictionary of column names and their corresponding values, splits the values in the
        column, and then changes the data types of the new columns

        :param mapper: a dictionary of dictionaries. The keys are the columns to be split, and the values
        are dictionaries with the following keys:
        :type mapper: dict[str, dict[str, str]]
        """
        for column, values in mapper.items():
            self.df[values["cols"]] = self.df[column].str.split(values["delimiter"], expand=True)
            self._change_dtypes(dict(zip(values["cols"], values["dtypes"])))
            self.df.drop(column, axis=1, inplace=True)

    def _hash_calc(self) -> None:
        """
        It takes a dataframe and returns a new dataframe with a new column called "id" that contains a hash
        of the dataframe
        """
        self.df["id"] = hash_pandas_object(self.df)

    def _change_dtypes(self, custom_mapper=dtypes_mapper) -> None:
        """
        It takes a dictionary of column names and their corresponding data types, and then changes the
        data types of the columns in the dataframe to the ones specified in the dictionary.

        :param custom_mapper: a dictionary of column names and their corresponding dtypes
        """
        for col, dtype in custom_mapper.items():
            self.df[col] = self.df[col].astype(dtype)
