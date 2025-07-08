from datetime import UTC, datetime

import pytest

from api.errors.blog_post_errors import PostNotFoundError
from api.models.blog_post_models import BlogPostCreate, BlogPostPatch, BlogPostUpdate
from api.repository.blog_post_repository import BlogPostRepository


class TestBlogPostRepository:

    def test_class_import_and_instantiation(self):
        assert BlogPostRepository is not None
        repo = BlogPostRepository()
        assert repo.db == {}

    def test_get_next_id_increments_properly(self):
        repo = BlogPostRepository()
        assert repo._get_next_id() == 1

        repo.db[1] = "test"
        assert repo._get_next_id() == 2

        repo.db[2] = "test"
        assert repo._get_next_id() == 3

    def test_get_current_datetime_returns_utc_datetime(self):
        repo = BlogPostRepository()
        now = datetime.now(UTC)
        repo_now = repo._get_current_datetime()
        assert isinstance(repo_now, datetime)
        assert abs((repo_now - now).total_seconds()) < 1

    # === CREATE ===

    def test_create_blog_post_adds_to_db(self):
        repo = BlogPostRepository()
        post = BlogPostCreate(title="post1", content="content1", author="author1")
        repo.create_blog_post(post)

        assert 1 in repo.db
        created = repo.db[1]
        assert created.title == "post1"
        assert created.content == "content1"
        assert created.author == "author1"

    def test_create_multiple_blog_posts_increment_id(self):
        repo = BlogPostRepository()
        post1 = BlogPostCreate(title="post1", content="content1", author="author1")
        post2 = BlogPostCreate(title="post2", content="content2", author="author2")

        repo.create_blog_post(post1)
        repo.create_blog_post(post2)

        assert 1 in repo.db
        assert 2 in repo.db
        assert repo.db[2].title == "post2"

    # === GET ===

    def test_get_blog_post_returns_correct_post(self):
        repo = BlogPostRepository()
        post = BlogPostCreate(title="post", content="content", author="author")
        repo.create_blog_post(post)

        result = repo.get_blog_post(1)
        assert result.title == "post"
        assert result.content == "content"
        assert result.author == "author"

    def test_get_blog_post_raises_if_not_found(self):
        repo = BlogPostRepository()
        with pytest.raises(PostNotFoundError):
            repo.get_blog_post(999)

    def test_get_all_blog_posts_returns_list(self):
        repo = BlogPostRepository()
        repo.create_blog_post(BlogPostCreate(title="post1", content="content1", author="author1"))
        repo.create_blog_post(BlogPostCreate(title="post2", content="content2", author="author2"))

        all_posts = repo.get_all_blog_posts()
        assert len(all_posts) == 2
        assert all_posts[0].title == "post1"
        assert all_posts[1].title == "post2"

    def test_get_all_blog_posts_returns_empty_list(self):
        repo = BlogPostRepository()
        assert repo.get_all_blog_posts() == []

    # === DELETE ===

    def test_delete_blog_post_removes_post(self):
        repo = BlogPostRepository()
        repo.create_blog_post(BlogPostCreate(title="post", content="content", author="author"))
        repo.delete_blog_post(1)
        assert repo.db == {}

    def test_delete_blog_post_raises_if_not_found(self):
        repo = BlogPostRepository()
        with pytest.raises(PostNotFoundError):
            repo.delete_blog_post(1)

    # === UPDATE ===

    def test_update_blog_post_replaces_all_fields(self):
        repo = BlogPostRepository()
        repo.create_blog_post(BlogPostCreate(title="post", content="content", author="author"))

        update = BlogPostUpdate(title="post2", content="content2", author="author2")
        repo.update_blog_post(1, update)

        updated = repo.db[1]
        assert updated.title == "post2"
        assert updated.content == "content2"
        assert updated.author == "author2"

    def test_update_blog_post_raises_if_not_found(self):
        repo = BlogPostRepository()
        with pytest.raises(PostNotFoundError):
            repo.update_blog_post(1, BlogPostUpdate(title="post2", content="content2", author="author2"))

    # === PATCH ===

    def test_patch_blog_post_updates_title_only(self):
        repo = BlogPostRepository()
        repo.create_blog_post(BlogPostCreate(title="post1", content="content1", author="author1"))

        patch = BlogPostPatch(title="post2")
        repo.patch_blog_post(1, patch)

        updated = repo.db[1]
        assert updated.title == "post2"
        assert updated.content == "content1"
        assert updated.author == "author1"

    def test_patch_blog_post_updates_content_only(self):
        repo = BlogPostRepository()
        repo.create_blog_post(BlogPostCreate(title="post1", content="content1", author="author1"))

        patch = BlogPostPatch(content="content2")
        repo.patch_blog_post(1, patch)

        updated = repo.db[1]
        assert updated.title == "post1"
        assert updated.content == "content2"
        assert updated.author == "author1"

    def test_patch_blog_post_updates_author_only(self):
        repo = BlogPostRepository()
        repo.create_blog_post(BlogPostCreate(title="post1", content="content1", author="author1"))

        patch = BlogPostPatch(author="author2")
        repo.patch_blog_post(1, patch)

        updated = repo.db[1]
        assert updated.title == "post1"
        assert updated.content == "content1"
        assert updated.author == "author2"

    def test_patch_blog_post_raises_if_not_found(self):
        repo = BlogPostRepository()
        with pytest.raises(PostNotFoundError):
            repo.patch_blog_post(1, BlogPostPatch(title="post1"))
