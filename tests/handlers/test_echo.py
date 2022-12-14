from unittest.mock import AsyncMock

import pytest

from trade_telegram_bot.bot import echo


@pytest.mark.asyncio
async def test_echo_handler():
    text_mock = "test123"
    message_mock = AsyncMock(text=text_mock)
    await echo(message=message_mock)
    message_mock.answer.assert_called_with(text_mock)
