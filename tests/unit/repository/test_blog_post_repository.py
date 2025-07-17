from datetime import UTC, datetime

import pytest

from api.errors.blog_post_errors import PostNotFoundError
from api.models.blog_post_models import BlogPostCreate, BlogPostPatch, BlogPostUpdate
from api.repository.blog_post_repository import BlogPostRepository


class TestBlogPostRepository:

    def test_class_import_and_instantiation(self, test_repository):
        assert BlogPostRepository is not None
        assert test_repository.session is not None

    def test_get_current_datetime_returns_utc_datetime(self, test_repository):
        now = datetime.now(UTC)
        repo_now = test_repository._get_current_datetime()
        assert isinstance(repo_now, datetime)
        assert abs((repo_now - now).total_seconds()) < 1

    # === CREATE ===

    def test_create_blog_post_adds_to_db(self, test_repository):
        post = BlogPostCreate(title="post1", content="content1", author="author1")
        created = test_repository.create_blog_post(post)

        assert created.title == "post1"
        assert created.content == "content1"
        assert created.author == "author1"
        assert created.post_id is not None

    def test_create_multiple_blog_posts_increment_id(self, test_repository):
        post1 = BlogPostCreate(title="post1", content="content1", author="author1")
        post2 = BlogPostCreate(title="post2", content="content2", author="author2")

        created1 = test_repository.create_blog_post(post1)
        created2 = test_repository.create_blog_post(post2)

        assert created1.post_id != created2.post_id
        assert created2.title == "post2"

    # === GET ===

    def test_get_blog_post_returns_correct_post(self, test_repository):
        post = BlogPostCreate(title="post", content="content", author="author")
        created = test_repository.create_blog_post(post)

        result = test_repository.get_blog_post(created.post_id)
        assert result.title == "post"
        assert result.content == "content"
        assert result.author == "author"

    def test_get_blog_post_raises_if_not_found(self, test_repository):
        with pytest.raises(PostNotFoundError):
            test_repository.get_blog_post(999)

    def test_get_all_blog_posts_returns_list(self, test_repository):
        test_repository.create_blog_post(BlogPostCreate(title="post1", content="content1", author="author1"))
        test_repository.create_blog_post(BlogPostCreate(title="post2", content="content2", author="author2"))

        all_posts = test_repository.get_all_blog_posts()
        assert len(all_posts) == 2
        # Verifica se os posts estão na lista (ordem pode variar)
        titles = [post.title for post in all_posts]
        assert "post1" in titles
        assert "post2" in titles

    def test_get_all_blog_posts_returns_empty_list(self, test_repository):
        assert test_repository.get_all_blog_posts() == []

    # === DELETE ===

    def test_delete_blog_post_removes_post(self, test_repository):
        created = test_repository.create_blog_post(BlogPostCreate(title="post", content="content", author="author"))
        test_repository.delete_blog_post(created.post_id)
        
        with pytest.raises(PostNotFoundError):
            test_repository.get_blog_post(created.post_id)

    def test_delete_blog_post_raises_if_not_found(self, test_repository):
        with pytest.raises(PostNotFoundError):
            test_repository.delete_blog_post(1)

    # === UPDATE ===

    def test_update_blog_post_replaces_all_fields(self, test_repository):
        created = test_repository.create_blog_post(BlogPostCreate(title="post", content="content", author="author"))

        update = BlogPostUpdate(title="post2", content="content2", author="author2")
        updated = test_repository.update_blog_post(created.post_id, update)

        assert updated.title == "post2"
        assert updated.content == "content2"
        assert updated.author == "author2"

    def test_update_blog_post_raises_if_not_found(self, test_repository):
        with pytest.raises(PostNotFoundError):
            test_repository.update_blog_post(1, BlogPostUpdate(title="post2", content="content2", author="author2"))

    # === PATCH ===

    def test_patch_blog_post_updates_title_only(self, test_repository):
        created = test_repository.create_blog_post(BlogPostCreate(title="post1", content="content1", author="author1"))

        patch = BlogPostPatch(title="post2")
        updated = test_repository.patch_blog_post(created.post_id, patch)

        assert updated.title == "post2"
        assert updated.content == "content1"
        assert updated.author == "author1"

    def test_patch_blog_post_updates_content_only(self, test_repository):
        created = test_repository.create_blog_post(BlogPostCreate(title="post1", content="content1", author="author1"))

        patch = BlogPostPatch(content="content2")
        updated = test_repository.patch_blog_post(created.post_id, patch)

        assert updated.title == "post1"
        assert updated.content == "content2"
        assert updated.author == "author1"

    def test_patch_blog_post_updates_author_only(self, test_repository):
        created = test_repository.create_blog_post(BlogPostCreate(title="post1", content="content1", author="author1"))

        patch = BlogPostPatch(author="author2")
        updated = test_repository.patch_blog_post(created.post_id, patch)

        assert updated.title == "post1"
        assert updated.content == "content1"
        assert updated.author == "author2"

    def test_patch_blog_post_raises_if_not_found(self, test_repository):
        with pytest.raises(PostNotFoundError):
            test_repository.patch_blog_post(1, BlogPostPatch(title="post1"))
