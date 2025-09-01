from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "My SaaS API"
    API_V1_STR: str = "/api/v1"
    DATABASE_TYPE: str = "sqlite"
    DATABASE_URI: str
    SECRET_KEY: str = "mysec"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

    def get_option(self):
        if self.DATABASE_TYPE == "sqlite":
            return {
                "connect_args":{"check_same_thread":False }
            }
        else:
            return

settings = Settings()
