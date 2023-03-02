import redis

from trade_telegram_bot.core.envs import env_vars

redis_client = redis.Redis(
    host=env_vars.cache.host,
    port=env_vars.cache.port,
    password=env_vars.cache.passwd,
    ssl=True,
)
