import logging

from aiogram.types import ContentTypes
from aiogram.utils.executor import start_webhook

from trade_telegram_bot.core.envs import env_vars
from trade_telegram_bot.core.manage import bot, dp
from trade_telegram_bot.handlers.echo import echo
from trade_telegram_bot.handlers.input_csv import processing_input_csv
from trade_telegram_bot.utils.consts import PROJECT_VERSION

logging.basicConfig(level=logging.INFO)


async def on_startup(dp):
    """
    It sets the webhook for the bot

    :param dp: Dispatcher object
    """
    logging.info(f"{PROJECT_VERSION}: Set webhook")
    await bot.set_webhook(env_vars.telegram.webhook_url, drop_pending_updates=True)


if __name__ == "__main__":
    dp.register_message_handler(processing_input_csv, content_types=ContentTypes.DOCUMENT)
    dp.register_message_handler(echo)
    start_webhook(
        dispatcher=dp,
        webhook_path=f"/{env_vars.telegram.token}",
        on_startup=on_startup,
        skip_updates=True,
        host=env_vars.telegram.webapp_host,
        port=env_vars.telegram.webapp_port,
    )
