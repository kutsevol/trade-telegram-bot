import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook

from trade_telegram_bot.core.envs import env_vars

VERSION = "Version 1.0.1"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=env_vars.telegram_token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler()
async def echo(message: types.Message):
    logging.info(f"{VERSION}: executing echo function...")
    await message.answer(message.text)


async def on_startup(dp):
    logging.info(f"{VERSION}: Set webhook...")
    await bot.set_webhook(env_vars.webhook_url, drop_pending_updates=True)


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=f"/{env_vars.telegram_token}",
        on_startup=on_startup,
        skip_updates=True,
        host=env_vars.webapp_host,
        port=env_vars.webapp_port,
    )
