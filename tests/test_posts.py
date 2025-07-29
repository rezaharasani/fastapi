import pytest
from app import schemas
from fastapi import status, HTTPException

"""
    For getting all posts in authorized and unauthorized user
"""


def test_authorized_user_get_all_posts(authorized_client, test_posts):
    response = authorized_client.get("/posts/")
    mapped_posts = map(
        lambda post: schemas.PostOut(**post.dict()), response.json()
    )
    assert len(response.json()) == len(test_posts)
    assert response.status_code == 200


def test_unauthorized_user_get_all_posts(client, test_posts):
    response = client.get("/posts/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


"""
    For getting one post in authorized and unauthorized user
"""


def test_authorized_user_get_one_post(authorized_client, test_posts):
    response = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**response.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.title == test_posts[0].title
    assert post.Post.content == test_posts[0].content
    assert response.status_code == status.HTTP_200_OK


def test_authorized_user_get_one_post_not_exist(authorized_client, test_posts):
    response = authorized_client.get("/posts/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_unauthorized_user_get_one_post(client, test_posts):
    response = client.get(
        f"/posts/{test_posts[0].id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize("title, content, published", [
    ("1st new post", "First new content", True),
    ("2nd new post", "2nd new content", False),
    ("3rd new post", "3rd new content", True)
])
def test_authorized_user_create_post(authorized_client, test_user, test_posts, title, content, published):
    response = authorized_client.post("/posts/", json={
        "title": title, "content": content, "published": published})
    created_post = schemas.Post(**response.json())
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user['id']
    assert response.status_code == status.HTTP_201_CREATED


def test_authorized_user_create_post_default_published_true(authorized_client, test_user, test_posts):
    response = authorized_client.post("/posts/", json={
        "title": "Published parameter Post", "content": "Test default published equal True"
    })
    created_post = schemas.Post(**response.json())
    assert response.status_code == status.HTTP_201_CREATED
    assert created_post.title == "Published parameter Post"
    assert created_post.content == "Test default published equal True"
    assert created_post.published == True
    assert created_post.owner_id == test_user['id']
    assert response.status_code == status.HTTP_201_CREATED


def test_unauthorized_user_create_post(client, test_user, test_posts):
    response = client.post("/posts/", json={
        "title": "Published parameter Post", "content": "Test default published equal True"
    })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_unauthorized_user_delete_post(client, test_user, test_posts):
    response = client.delete(
        f"/posts/{test_posts[0].id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_authorized_user_delete_post(authorized_client, test_user, test_posts):
    response = authorized_client.delete(
        f"/posts/{test_posts[0].id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_authorized_user_delete_post_not_exist(authorized_client, test_user, test_posts):
    response = authorized_client.delete(
        f"/posts/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_other_user_post(authorized_client, test_user, test_user2, test_posts):
    response = authorized_client.delete(
        f"/posts/{test_posts[3].id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_authorized_user_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "New title",
        "content": "New content",
        "published": True,
        "owner_id": test_posts[0].id
    }
    response = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.Post(**response.json())

    assert response.status_code == status.HTTP_200_OK
    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]
    assert updated_post.published == data["published"]
    assert updated_post.owner_id == data["owner_id"]


def test_update_other_user_post(authorized_client, test_user, test_user2, test_posts):
    data = {
        "title": "New title",
        "content": "New content",
        "published": True,
        "owner_id": test_posts[3].id
    }
    response = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_unauthorized_user_update_post(client, test_user, test_posts):
    data = {
        "title": "New title",
        "content": "New content",
        "published": True,
        "owner_id": test_posts[0].id
    }
    response = client.put(f"/posts/{test_posts[0].id}", json=data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_authorized_user_update_post_not_exist(authorized_client, test_user, test_posts):
    data = {
        "title": "New title",
        "content": "New content",
        "published": True,
        "owner_id": test_posts[0].id
    }
    response = authorized_client.put(f"/posts/999", json=data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
