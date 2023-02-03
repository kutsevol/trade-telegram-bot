from trade_telegram_bot.utils.consts import EnvVars

env_vars = EnvVars()

mysql_db_uri = f"mysql+mysqldb://{env_vars.db.user}:{env_vars.db.passwd}@{env_vars.db.host}/{env_vars.db.db_name}"
