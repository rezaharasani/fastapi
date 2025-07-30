import pytest
from fastapi import status
from fastapi.testclient import TestClient

from sqlalchemy import create_engine, false
from sqlalchemy.orm import sessionmaker

from app import models
from app.main import app
from app.config import settings
from app.database import get_db, Base
from app.oauth2 import create_access_token

SQLALCHEMY_DATABASE_URL = (f"postgresql://"
                           f"{settings.POSTGRES_USER}:"
                           f"{settings.POSTGRES_PASSWORD}@"
                           f"{settings.POSTGRES_SERVER}:"
                           f"{settings.POSTGRES_PORT}/"
                           f"{settings.POSTGRES_DB}_test")

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password123@127.0.0.1:5432/fastapi_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    user_data = {
        "email": "test@localhost.com",
        "password": "password123",
        "phone_number": "09111234567"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == status.HTTP_201_CREATED
    new_user = response.json()
    new_user["password"] = user_data["password"]
    return new_user


@pytest.fixture
def test_user2(client):
    user_data = {
        "email": "user@localhost.com",
        "password": "password123",
        "phone_number": "09117654321"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == status.HTTP_201_CREATED
    new_user = response.json()
    new_user["password"] = user_data["password"]
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user["id"]})


@pytest.fixture
def authorized_client(client, token):
    client.headers.update({"Authorization": f"Bearer {token}"})
    return client


@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [{
        "title": "First Post",
        "content": "First Content",
        "owner_id": test_user["id"]
    }, {
        "title": "2nd Post",
        "content": "2nd Content",
        "owner_id": test_user["id"]
    }, {
        "title": "3rd Post",
        "content": "3rd Content",
        "owner_id": test_user["id"]
    }, {
        "title": "1st Post of user 2",
        "content": "1st Content of user 2",
        "owner_id": test_user2["id"]
    }]

    def create_post_model(post):
        return models.Post(**post)

    posts_mapped = list(map(create_post_model, posts_data))
    session.add_all(posts_mapped)
    session.commit()

    posts = session.query(models.Post).all()
    return posts
