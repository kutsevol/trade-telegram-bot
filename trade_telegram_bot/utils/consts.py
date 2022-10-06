from pathlib import PurePath
from typing import Optional

from pydantic import BaseSettings, Field, validator

BASE_DIR = PurePath(__file__).parent.parent
SECRETS_DIR = "secret_vars"
ENV_FILE = ".env"


class EnvVars(BaseSettings):
    telegram_token: str = Field(..., env="TELEGRAM_TOKEN")
    webhook_host: str = Field(..., env="WEBHOOK_HOST")
    webapp_host: str = Field(..., env="WEBAPP_HOST")
    webapp_port: int = Field(..., env="WEBAPP_PORT")

    webhook_url: Optional[str]

    class Config:
        case_sensitive = False
        env_file = BASE_DIR.joinpath(SECRETS_DIR).joinpath(ENV_FILE)

    @validator("webhook_url", always=True)
    def validate_webhook_url(cls, value, values):
        return f"{values['webhook_host']}/{values['telegram_token']}"
