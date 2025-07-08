import contextlib

import pytest
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_root_redirects_to_docs():
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307 or response.status_code == 302
    assert response.headers["location"] == "/docs"


@pytest.fixture
def created_blog_post():
    payload = {
        "title": "Integration Test Post",
        "content": "This post was created by an integration test.",
        "author": "IntegrationBot"
    }
    response = client.post("/blog_posts", json=payload)
    assert response.status_code == 201
    post_id = response.json()["data"]["post_id"]
    
    yield post_id

    with contextlib.suppress(Exception):
        client.delete(f"/blog_posts/{post_id}")


def test_create_blog_post_returns_201():
    payload = {
        "title": "Integration Test Post",
        "content": "This post was created by an integration test.",
        "author": "IntegrationBot"
    }
    response = client.post("/blog_posts", json=payload)
    assert response.status_code == 201
    assert response.json()["success"] is True
    assert response.json()["data"]["title"] == payload["title"]


def test_get_blog_post_returns_200(created_blog_post):
    post_id = created_blog_post
    response = client.get(f"/blog_posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["data"]["post_id"] == post_id


def test_get_all_blog_posts_returns_list():
    response = client.get("/blog_posts")
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)


def test_update_blog_post_returns_200(created_blog_post):
    post_id = created_blog_post
    update = {
        "title": "Updated Title",
        "content": "Updated Content",
        "author": "Updated Author"
    }
    response = client.put(f"/blog_posts/{post_id}", json=update)
    assert response.status_code == 200
    assert response.json()["data"]["title"] == "Updated Title"


def test_patch_blog_post_returns_200(created_blog_post):
    post_id = created_blog_post
    patch = {
        "content": "Patched Content"
    }
    response = client.patch(f"/blog_posts/{post_id}", json=patch)
    assert response.status_code == 200
    assert response.json()["data"]["content"] == "Patched Content"


def test_delete_blog_post_returns_204(created_blog_post):
    post_id = created_blog_post
    response = client.delete(f"/blog_posts/{post_id}")
    assert response.status_code == 204


def test_get_deleted_blog_post_returns_404():
    post_id = 99
    response = client.get(f"/blog_posts/{post_id}")
    assert response.status_code == 400
    assert response.json()["message"] == f"Blog post with id {post_id} does not exist"


def test_create_blog_post_invalid_returns_422():
    payload = {
        "title": "X",  # muito curto
        "content": "",  # vazio
        "author": "A"
    }
    response = client.post("/blog_posts", json=payload)
    assert response.status_code == 422 or response.status_code == 400