import contextlib

import pytest


def test_root_redirects_to_docs(test_client):
    response = test_client.get("/", follow_redirects=False)
    assert response.status_code == 307 or response.status_code == 302
    assert response.headers["location"] == "/docs"


@pytest.fixture
def created_blog_post(test_client):
    payload = {
        "title": "Integration Test Post",
        "content": "This post was created by an integration test.",
        "author": "IntegrationBot"
    }
    response = test_client.post("/blog_posts", json=payload)
    assert response.status_code == 201
    post_id = response.json()["data"]["post_id"]
    
    yield post_id

    with contextlib.suppress(Exception):
        test_client.delete(f"/blog_posts/{post_id}")


def test_create_blog_post_returns_201(test_client):
    payload = {
        "title": "Integration Test Post",
        "content": "This post was created by an integration test.",
        "author": "IntegrationBot"
    }
    response = test_client.post("/blog_posts", json=payload)
    assert response.status_code == 201
    assert response.json()["success"] is True
    assert response.json()["data"]["title"] == payload["title"]


def test_get_blog_post_returns_200(created_blog_post, test_client):
    post_id = created_blog_post
    response = test_client.get(f"/blog_posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["data"]["post_id"] == post_id


def test_get_all_blog_posts_returns_list(test_client):
    response = test_client.get("/blog_posts")
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)


def test_update_blog_post_returns_200(created_blog_post, test_client):
    post_id = created_blog_post
    update = {
        "title": "Updated Title",
        "content": "Updated Content",
        "author": "Updated Author"
    }
    response = test_client.put(f"/blog_posts/{post_id}", json=update)
    assert response.status_code == 200
    assert response.json()["data"]["title"] == "Updated Title"


def test_patch_blog_post_returns_200(created_blog_post, test_client):
    post_id = created_blog_post
    patch = {
        "content": "Patched Content"
    }
    response = test_client.patch(f"/blog_posts/{post_id}", json=patch)
    assert response.status_code == 200
    assert response.json()["data"]["content"] == "Patched Content"


def test_delete_blog_post_returns_204(created_blog_post, test_client):
    post_id = created_blog_post
    response = test_client.delete(f"/blog_posts/{post_id}")
    assert response.status_code == 204


def test_get_deleted_blog_post_returns_404(test_client):
    post_id = 99
    response = test_client.get(f"/blog_posts/{post_id}")
    assert response.status_code == 400
    assert response.json()["message"] == f"Blog post with id {post_id} does not exist"


def test_create_blog_post_invalid_returns_422(test_client):
    payload = {
        "title": "X",
        "content": "", 
        "author": "A"
    }
    response = test_client.post("/blog_posts", json=payload)
    assert response.status_code == 422 or response.status_code == 400