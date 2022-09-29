import secrets
from pathlib import Path
from typing import List, Optional

from pydantic import AnyHttpUrl, BaseSettings

PROJECT_TOP = Path(__file__).parent.parent


class Settings(BaseSettings):
    PROJECT_NAME: str = "fastAPITemplate"
    API_STR: str = "/api"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = ""
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str

    # celery (queue server) setting
    CELERY_BROKER_URL: str = "redis://localhost:6379"
    CELERY_BACKEND_URL: str = "redis://localhost:6379"

    class Config:
        case_sensitive = True
        env_file = PROJECT_TOP.parent / ".env"
        env_file_encoding = "utf-8"


settings = Settings()
