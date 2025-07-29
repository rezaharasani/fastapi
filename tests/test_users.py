import pytest
from fastapi import status
from jose import jwt
from app import schemas
from app.config import settings
from .conftest import client, session, test_user


def test_create_user(client):
    response = client.post("/users/", json={
        "email": "user1@localhost.com",
        "password": "password123",
        "phone_number": "09123456789"
    })
    new_user = schemas.UserOut(**response.json())
    assert response.status_code == status.HTTP_201_CREATED
    assert new_user.email == "user1@localhost.com"


def test_login_user(client, test_user):
    response = client.post("/login", data={
        "username": test_user["email"],
        "password": test_user["password"]
    })
    login_response = schemas.Token(**response.json())
    payload = jwt.decode(
        login_response.access_token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
    )
    user_id = payload["user_id"]
    assert user_id == test_user["id"]
    assert login_response.token_type == "bearer"
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize("email, password, status_code", [
    ("wrong@localhost.com", "password123", 403),
    ("test@localhost.com", "wrong_password", 403),
    ("wrong@localhost.com", "wrong_password", 403),
    (None, "password123", 403),
    ("test@localhost.com", None, 403)
])
def test_incorrect_login(client, test_user, email, password, status_code):
    response = client.post("/login", data={
        "username": email,
        "password": password
    })
    assert response.status_code == status_code
