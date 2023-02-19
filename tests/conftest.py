import pytest
import sqlalchemy
from alembic.command import upgrade
from alembic.config import Config
from sqlalchemy.orm import sessionmaker
from testcontainers.mysql import MySqlContainer
from testcontainers.redis import RedisContainer

from trade_telegram_bot.utils.consts import ALEMBIC_CONFIG_FILE, BASE_DIR


@pytest.fixture
def db_session(mysql_engine):
    db_session = sessionmaker(bind=mysql_engine)()
    upgrade(Config(BASE_DIR.parent.joinpath(ALEMBIC_CONFIG_FILE)), "head")
    yield db_session
    db_session.close()


@pytest.fixture
def mysql_engine(monkeypatch):
    with MySqlContainer() as mysql:
        mysql_db_uri = mysql.get_connection_url()
        monkeypatch.setattr("trade_telegram_bot.core.envs.mysql_db_uri", mysql_db_uri)
        mysql_engine = sqlalchemy.create_engine(mysql_db_uri)
        yield mysql_engine
        mysql_engine.dispose()


@pytest.fixture
def redis_container(monkeypatch):
    with RedisContainer() as redis_client:
        client = redis_client.get_client()
        yield client
        client.close()
