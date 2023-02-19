from unittest.mock import AsyncMock

import pytest
from aiogram import Bot, types

from tests import TOKEN
from tests.data.types import MESSAGE
from trade_telegram_bot.bot import echo


@pytest.mark.asyncio
async def test_echo():
    _bot = Bot(TOKEN)
    _bot.send_message = AsyncMock(name="send_message")
    Bot.set_current(_bot)

    await echo(message=types.Message(**MESSAGE))
    _bot.send_message.assert_called()
