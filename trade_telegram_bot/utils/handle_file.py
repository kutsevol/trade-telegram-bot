from io import BytesIO

from aiogram import types

from trade_telegram_bot.core.manage import bot


async def load_file_from_user(message: types.Message) -> BytesIO:
    """
    It downloads the file from the Telegram server and returns it as a BytesIO object

    :param message: types.Message - the message that the user sent to the bot
    :type message: types.Message
    :return: A BytesIO object
    """
    file = await bot.get_file(message.document.file_id)

    obj = await bot.download_file(file.file_path)
    return obj
