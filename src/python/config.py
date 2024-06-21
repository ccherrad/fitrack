# pylint: disable=no-self-argument,no-self-use
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import PostgresDsn, field_validator, ValidationInfo
from pydantic_settings import BaseSettings 


class Settings(BaseSettings):
    ENV: Literal["TEST", "DEV", "PROD"] = "DEV"

    SQL_DB: str
    SQL_HOST: str
    SQL_PORT: str
    SQL_USERNAME: str
    SQL_PASSWORD: str
    SQL_SSL: Optional[bool] = False
    SQLALCHEMY_DATABASE_URI: Union[Optional[PostgresDsn], Optional[str]] = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], values: ValidationInfo) -> Any:
        if isinstance(v, str):
            print("Loading SQLALCHEMY_DATABASE_URI from .docker.env file ...")
            return v
        print("Creating SQLALCHEMY_DATABASE_URI from .env file ...")
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get("SQL_USERNAME"),
            password=values.data.get("SQL_PASSWORD"),
            host=values.data.get("SQL_HOST"),
            port=int(values.data.get("SQL_PORT")),
            path=f"{values.data.get('SQL_DB') or ''}",
        )

    class Config:
        env_file = ".env"

settings = Settings()
