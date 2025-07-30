from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_PORT: str = '5432'
    POSTGRES_OUT_PORT: str = '5444'
    POSTGRES_DB: str = 'postgres'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    PROJECT_VERSION: str = 'Testing'
    ENVIRONMENT: str = 'Development'

    NGINX_PORT: str = '80'

    OTEL_EXPORTER_OTLP_ENDPOINT: str
    OTEL_TRACES_EXPORTER: str
    OTEL_METRICS_EXPORTER: str
    JAEGER_UI_OUT_PORT: str
    OTLP_GRPC_OUT_PORT: str
    COLLECTOR_OTLP_ENABLED: bool = True

    class Config:
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
