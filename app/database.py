from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

SQLALCHEMY_DATABASE_URL = \
    (f"postgresql://"
     f"{settings.POSTGRES_USER}:"
     f"{settings.POSTGRES_PASSWORD}@"
     f"{settings.POSTGRES_SERVER}:"
     f"{settings.POSTGRES_PORT}/"
     f"{settings.POSTGRES_DB}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
