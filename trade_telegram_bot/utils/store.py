from trade_telegram_bot.core.cache import redis_client
from trade_telegram_bot.utils.consts import REDIS_KEY


def redis_cache(func):
    def wrapper(*args):
        df = args[0]
        if redis_client.exists(REDIS_KEY):
            non_cached_ids = set(df.id).difference({item.decode() for item in redis_client.smembers(REDIS_KEY)})
            df = df[df.id.isin(list(non_cached_ids))]
        func(df)
        if not df.empty:
            redis_client.sadd(REDIS_KEY, *set(df.id))

    return wrapper
