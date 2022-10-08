import logging

from aiogram import Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook

from trade_telegram_bot.core.envs import env_vars
from trade_telegram_bot.handlers.echo import echo
from trade_telegram_bot.utils.consts import pyproject_toml

logging.basicConfig(level=logging.INFO)

bot = Bot(token=env_vars.telegram_token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(dp):
    logging.info(f"{pyproject_toml['tool']['poetry']['version']}: Set webhook...")
    await bot.set_webhook(env_vars.webhook_url, drop_pending_updates=True)


if __name__ == "__main__":
    dp.register_message_handler(echo)
    start_webhook(
        dispatcher=dp,
        webhook_path=f"/{env_vars.telegram_token}",
        on_startup=on_startup,
        skip_updates=True,
        host=env_vars.webapp_host,
        port=env_vars.webapp_port,
    )
