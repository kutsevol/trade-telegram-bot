from pathlib import PurePath

import tomli
from pydantic import BaseSettings, Field, validator

BASE_DIR = PurePath(__file__).parent.parent
SECRETS_DIR = "secret_vars"
ENV_FILE = ".env"
PROJECT_FILE = "pyproject.toml"


class EnvVars(BaseSettings):
    telegram_token: str = Field(..., env="TELEGRAM_TOKEN")
    webhook_host: str = Field(..., env="WEBHOOK_HOST")
    webapp_host: str = Field(..., env="WEBAPP_HOST")
    webapp_port: int = Field(..., env="WEBAPP_PORT")

    webhook_url: str | None

    class Config:
        case_sensitive = False
        env_file = BASE_DIR.joinpath(SECRETS_DIR).joinpath(ENV_FILE)

    @validator("webhook_url", always=True)
    def validate_webhook_url(cls, value, values):
        return f"{values['webhook_host']}/{values['telegram_token']}"


with open(BASE_DIR.parent.joinpath(PROJECT_FILE), "rb") as file:
    pyproject_toml = tomli.load(file)
