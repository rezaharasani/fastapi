from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_PORT: str = '5432'
    POSTGRES_OUT_PORT: str = '5432'
    POSTGRES_DB: str = 'postgres'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    PROJECT_VERSION: str = 'Testing'

    NGINX_PORT: str = '80'

    class Config:
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
