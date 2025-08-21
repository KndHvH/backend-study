import pytest

from app.api.blog_post.models.blog_post_models import BlogPostBaseModel, BlogPostPatch


class TestBlogPostBaseModel:
    def test_class_import_and_instantiation(self):
        assert BlogPostBaseModel is not None
        model = BlogPostBaseModel(title="title", content="content", author="author")
        assert model.title == "title"
        assert model.content == "content"
        assert model.author == "author"
    
    def test_validate_fields(self):
        with pytest.raises(ValueError):
            BlogPostBaseModel(title="", content="content", author="author")
        with pytest.raises(ValueError):
            BlogPostBaseModel(title="title", content="", author="author")
        with pytest.raises(ValueError):
            BlogPostBaseModel(title="title", content="content", author="")
        with pytest.raises(ValueError):
            BlogPostBaseModel(title="title", content="aa", author="author")
        with pytest.raises(ValueError):
            BlogPostBaseModel(title="aa", content="content", author="author")
        with pytest.raises(ValueError):
            title = "a" * 101
            BlogPostBaseModel(title=title, content="content", author="author")
        with pytest.raises(ValueError):
            content = "a" * 1001
            BlogPostBaseModel(title="title", content=content, author="author")
        with pytest.raises(ValueError):
            author = "a" * 101
            BlogPostBaseModel(title="title", content="content", author=author)

    def test_validate_fields_with_none_value(self):
        # Testa o comportamento com valores None usando BlogPostPatch
        patch_model = BlogPostPatch()
        assert patch_model.title is None
        assert patch_model.content is None
        assert patch_model.author is None
        
        # Testa com alguns campos None e outros preenchidos
        partial_model = BlogPostPatch(title="título teste", content=None, author="autor teste")
        assert partial_model.title == "título teste"
        assert partial_model.content is None
        assert partial_model.author == "autor teste"

    def test_validate_model(self):
        with pytest.raises(ValueError):
            BlogPostBaseModel(title="title", content="title", author="author")
        with pytest.raises(ValueError):
            BlogPostBaseModel(title="title", content="content", author="title")
        with pytest.raises(ValueError):
            BlogPostBaseModel(title="title", content="content", author="content")
            