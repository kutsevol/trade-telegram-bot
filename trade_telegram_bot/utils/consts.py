from pathlib import PurePath

import tomli
from pydantic import BaseSettings, Field, validator

BASE_DIR = PurePath(__file__).parent.parent
SECRETS_DIR = "secret_vars"
ENV_FILE = ".env"
PROJECT_FILE = "pyproject.toml"


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


class EnvVars:
    telegram: TelegramVars = TelegramVars()
    db: DBVars = DBVars()


with open(BASE_DIR.parent.joinpath(PROJECT_FILE), "rb") as file:
    pyproject_toml = tomli.load(file)
