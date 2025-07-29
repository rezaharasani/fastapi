import pytest
from fastapi import status
from app import models


@pytest.fixture
def test_vote(test_posts, session, test_user):
    new_vote = models.Vote(
        post_id=test_posts[0].id, user_id=test_user['id']
    )
    session.add(new_vote)
    session.commit()


def test_authorized_user_vote_on_post(authorized_client, test_posts):
    response = authorized_client.post(
        "/vote/", json={"post_id": test_posts[0].id, "dir": 1})
    assert response.status_code == status.HTTP_201_CREATED


def test_authorized_user_vote_on_post_not_exist(authorized_client, test_posts):
    response = authorized_client.post(
        "/vote/", json={"post_id": 999, "dir": 1})
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_authorized_user_vote_twice_post(authorized_client, test_posts, test_vote):
    response = authorized_client.post(
        "/vote/", json={"post_id": test_posts[0].id, "dir": 1})
    assert response.status_code == status.HTTP_409_CONFLICT


def test_authorized_user_delete_vote(authorized_client, test_posts, test_vote):
    response = authorized_client.post(
        "/vote/", json={"post_id": test_posts[0].id, "dir": 0})
    assert response.status_code == status.HTTP_201_CREATED


def test_authorized_user_delete_vote_not_exist(authorized_client, test_posts):
    response = authorized_client.post(
        "/vote/", json={"post_id": test_posts[0].id, "dir": 0})
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_unauthorized_user_vote_on_post(client, test_posts):
    response = client.post(
        "/vote/", json={"post_id": test_posts[0].id, "dir": 1})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
