from aiogram import types


async def echo(message: types.Message):
    """
    It takes a message, and sends the same message back to the user

    :param message: types.Message - the message object
    :type message: types.Message
    """
    await message.answer(message.text)
