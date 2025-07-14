from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Settings(BaseSettings):
    postgres_user: Optional[str] = Field(None, alias="POSTGRES_USER")
    postgres_password: Optional[str] = Field(None, alias="POSTGRES_PASSWORD")
    postgres_db: Optional[str] = Field(None, alias="POSTGRES_DB")
    postgres_host: Optional[str] = Field(None, alias="POSTGRES_HOST")
    postgres_port: Optional[int] = Field(None, alias="POSTGRES_PORT")
    database_url: str = Field(default="", alias="DATABASE_URL")

    model_config = {
        "env_file": ".env",
        "populate_by_name": True,
        "extra": "allow",
    }

    @property
    def DATABASE_URL(self) -> str:
        if self.database_url:
            return self.database_url
        return (
            f"postgresql+asyncpg://{self.postgres_user}:"
            f"{self.postgres_password}@"
            f"{self.postgres_host}:"
            f"{self.postgres_port}/"
            f"{self.postgres_db}"
        )


settings = Settings()
