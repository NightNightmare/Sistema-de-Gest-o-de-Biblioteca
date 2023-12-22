from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str = "postgres"
    DB_HOST: str = "localhost"
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres-fastapi"


settings = Settings()