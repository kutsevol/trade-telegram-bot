from unittest.mock import AsyncMock

import pytest
from aiogram import Bot, types
from sqlalchemy import select

from tests import TOKEN
from tests.data.types import MESSAGE_WITH_DOCUMENT
from trade_telegram_bot.bot import processing_input_csv
from trade_telegram_bot.models.sweepcast import Sweepcast
from trade_telegram_bot.utils.consts import REDIS_KEY


@pytest.mark.asyncio
async def test_processing_input_csv(mysql_engine, db_session, redis_container, monkeypatch):
    monkeypatch.setattr("trade_telegram_bot.etl.loader.db_engine", mysql_engine)
    monkeypatch.setattr("trade_telegram_bot.utils.store.redis_client", redis_container)

    _bot = Bot(TOKEN)
    _bot.send_message = AsyncMock(name="send_message")
    Bot.set_current(_bot)

    await processing_input_csv(message=types.Message(**MESSAGE_WITH_DOCUMENT))

    db_records = db_session.execute(select(Sweepcast)).fetchall()
    cache_records = redis_container.smembers(REDIS_KEY)

    assert len(cache_records) == len(db_records)
