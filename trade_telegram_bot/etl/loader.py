import logging

import pandas as pd

from trade_telegram_bot.core.db import db_engine
from trade_telegram_bot.utils.consts import PROJECT_VERSION
from trade_telegram_bot.utils.store import redis_cache

logging.basicConfig(level=logging.INFO)


@redis_cache
def load_df_to_db(df: pd.DataFrame) -> None:
    """
    Load a dataframe to a database table

    :param df: pd.DataFrame - the dataframe to be saved to the database
    :type df: pd.DataFrame
    """
    logging.info(f"{PROJECT_VERSION}: Prepare to save {df.shape[0]} rows of data")
    df.to_sql("sweepcast", db_engine, if_exists="append", index=False)
