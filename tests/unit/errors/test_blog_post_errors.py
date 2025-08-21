from app.api.blog_post.errors.blog_post_errors import PostAlreadyExistsError, PostError, PostNotFoundError


class TestPostError:
    def test_post_error_initialization(self):
        error = PostError(123)
        assert error.post_id == 123
        assert error.message == "Error related to post id 123"


class TestPostNotFoundError:
    def test_post_not_found_error_initialization(self):
        error = PostNotFoundError(123)
        assert error.post_id == 123
        assert error.message == "Blog post with id 123 does not exist"


class TestPostAlreadyExistsError:
    def test_post_already_exists_error_initialization(self):
        error = PostAlreadyExistsError(123)
        assert error.post_id == 123
        assert error.message == "Blog post with id 123 already exists" 