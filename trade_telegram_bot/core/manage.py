from aiogram import Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher

from trade_telegram_bot.core.envs import env_vars

bot = Bot(token=env_vars.telegram.token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
