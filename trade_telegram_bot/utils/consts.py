from pathlib import PurePath

import tomli
from pydantic import BaseSettings, Field, validator

BASE_DIR = PurePath(__file__).parent.parent
SECRETS_DIR = "secret_vars"
ENV_FILE = ".env"
ALEMBIC_CONFIG_FILE = "alembic.ini"
PROJECT_FILE = "pyproject.toml"
TABLE_NAME = "sweepcast"
REDIS_KEY = "hashes"


class BaseVars(BaseSettings):
    class Config:
        case_sensitive = False
        env_file = BASE_DIR.joinpath(SECRETS_DIR).joinpath(ENV_FILE)


class DBVars(BaseVars):
    host: str = Field(..., env="DB_HOST")
    user: str = Field(..., env="DB_USERNAME")
    passwd: str = Field(..., env="DB_PASSWORD")
    db_name: str = Field(..., env="DB_NAME")


class TelegramVars(BaseVars):
    token: str = Field(..., env="TELEGRAM_TOKEN")
    webhook_host: str = Field(..., env="WEBHOOK_HOST")
    webapp_host: str = Field(..., env="WEBAPP_HOST")
    webapp_port: int = Field(..., env="WEBAPP_PORT")
    webhook_url: str | None

    @validator("webhook_url", always=True)
    def validate_webhook_url(cls, value, values):
        return f"{values['webhook_host']}/{values['token']}"


class CacheVars(BaseVars):
    host: str = Field(..., env="REDIS_HOST")
    port: str = Field(..., env="REDIS_PORT")
    passwd: str = Field(..., env="REDIS_PASSWORD")


class EnvVars:
    telegram: TelegramVars = TelegramVars()
    db: DBVars = DBVars()
    cache: CacheVars = CacheVars()


with open(BASE_DIR.parent.joinpath(PROJECT_FILE), "rb") as file:
    pyproject_toml = tomli.load(file)

PROJECT_VERSION = pyproject_toml["tool"]["poetry"]["version"]


name_cols_mapper = {
    "Date Timestamp": "date_timestamp",
    "Ticker": "ticker",
    "Activity Type": "activity_type",
    "Put or Call": "put_or_call",
    "Sentiment": "sentiment",
    "SweepScore": "sweep_score",
    "Vol/OI Ratio": "vol_oi_ratio",
    "Strike Price": "strike_price",
    "Expiration": "expiration",
    "Premium": "premium",
    "Details": "details",
}

date_format_mapper = {"date_timestamp": "%m/%d %I:%M %p", "expiration": "%m/%d/%Y"}

split_values_mapper = {
    "vol_oi_ratio": {"delimiter": "/", "cols": ["volume", "open_interest"], "dtypes": [int, int]},
    "details": {"delimiter": "@", "cols": ["count", "price"], "dtypes": [int, float]},
}

dtypes_mapper = {
    "id": str,
}
