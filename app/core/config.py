from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    sentry_dsn: str
    debug: bool = True
    database_url: str

    class Config:
        env_file = "./.env"

settings = Settings()