import logging

from aiogram import types

from trade_telegram_bot.etl.extractor import extract_data_from_csv
from trade_telegram_bot.etl.loader import load_df_to_db
from trade_telegram_bot.etl.transformer import Transformer
from trade_telegram_bot.utils.consts import PROJECT_VERSION
from trade_telegram_bot.utils.handle_file import load_file_from_user

logging.basicConfig(level=logging.INFO)


async def processing_input_csv(message: types.Message) -> None:
    """
    We load the file from the user, extract the data from the csv, transform the data, and load the
    data to the database

    :param message: types.Message - this is the message that the user sent to the bot
    :type message: types.Message
    """
    logging.info(f"{PROJECT_VERSION}: Reading input file")
    file_obj = await load_file_from_user(message)

    logging.info(f"{PROJECT_VERSION}: Extract data from csv")
    df = extract_data_from_csv(file_obj)

    logging.info(f"{PROJECT_VERSION}: Transform data")
    transformer = Transformer(df)
    df = transformer.modify()

    logging.info(f"{PROJECT_VERSION}: Load dataset to DB")
    load_df_to_db(df)

    await message.answer("Data processed successfully")
