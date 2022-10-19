from sqlalchemy import create_engine

from trade_telegram_bot.core.envs import env_vars

db_engine = create_engine(
    url=f"mysql+mysqldb://{env_vars.db.user}:{env_vars.db.passwd}@{env_vars.db.host}/{env_vars.db.db_name}"
)
