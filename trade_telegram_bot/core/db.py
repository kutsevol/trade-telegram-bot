from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from trade_telegram_bot.core.envs import mysql_db_uri

db_engine = create_engine(url=mysql_db_uri)

session = sessionmaker(bind=db_engine)()
