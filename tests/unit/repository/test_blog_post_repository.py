from datetime import UTC, datetime
from api.models.blog_post_models import BlogPostCreate, BlogPostPatch, BlogPostUpdate
from api.repository.blog_post_repository import BlogPostRepository


class TestBlogPostRepository:    
    def test_import_blog_post_repository(self):        
        assert BlogPostRepository is not None   
        
    def test_instance_blog_post_repository(self):
        repo = BlogPostRepository()
        assert repo is not None
        assert repo.db == {}
        
    def test_get_next_id(self):
        repo = BlogPostRepository()
        assert repo._get_next_id() == 1
        
        repo.db[1] = 'test'
        assert repo._get_next_id() == 2
        
        repo.db[2] = 'test'
        assert repo._get_next_id() == 3
        assert repo._get_next_id() == 3
        
    def test_get_current_datetime(self):    
        repo = BlogPostRepository()
        assert repo._get_current_datetime is not None
        assert repo._get_current_datetime() == datetime.now(UTC)
        
        
    def test_create_blog_post(self):
        post = BlogPostCreate(
            title='post1',   
            content='content1',
            author='author1'
        )
        repo = BlogPostRepository()
        assert repo.db == {} 
        
        repo.create_blog_post(post)
        assert repo.db[1].title == 'post1'
        assert repo.db[1].content == 'content1'
        assert repo.db[1].author == 'author1'
        
        post = BlogPostCreate(
            title='post2',   
            content='content2',
            author='author2'
        )
        repo.create_blog_post(post)
        
        assert repo.db[2].title == 'post2'
        assert repo.db[2].content == 'content2'
        assert repo.db[2].author == 'author2'
        
    def test_update_blog_post(self):
        post = BlogPostCreate(
            title='post1',   
            content='content1',
            author='author1'
        )
        repo = BlogPostRepository()
        repo.create_blog_post(post)
        
        assert repo.db[1].title == 'post1'
        assert repo.db[1].content == 'content1'
        assert repo.db[1].author == 'author1'
        
        post = BlogPostUpdate(
            title='post2',   
            content='content2',
            author='author2'
        )
        repo.update_blog_post(1, post)
        
        assert repo.db[1].title == 'post2'
        assert repo.db[1].content == 'content2'
        assert repo.db[1].author == 'author2'

    def test_patch_blog_post(self):
        post = BlogPostCreate(
            title='post1',   
            content='content1',
            author='author1'
        )
        repo = BlogPostRepository()
        repo.create_blog_post(post)
        
        assert repo.db[1].title == 'post1' 
        assert repo.db[1].content == 'content1'
        assert repo.db[1].author == 'author1'
        
        post = BlogPostPatch(content='content2')
        repo.patch_blog_post(1, post)
        
        assert repo.db[1].title == 'post1'
        assert repo.db[1].content == 'content2'
        assert repo.db[1].author == 'author1'
        
        post = BlogPostPatch(title='post2')
        repo.patch_blog_post(1, post)
        
        assert repo.db[1].title == 'post2'
        assert repo.db[1].content == 'content2'
        assert repo.db[1].author == 'author1'
    
    def test_delete_blog_post(self):
        post = BlogPostCreate(
            title='post1',   
            content='content1',
            author='author1'
        )
        repo = BlogPostRepository()
        repo.create_blog_post(post)
        
        assert repo.db[1].title == 'post1'
        
        repo.delete_blog_post(1)
        assert repo.db == {}
        
    def test_get_blog_post(self):
        post = BlogPostCreate(
            title='post1',   
            content='content1',
            author='author1'
        )
        repo = BlogPostRepository()
        repo.create_blog_post(post)
        
        assert repo.get_blog_post(1).title == 'post1'
        assert repo.get_blog_post(1).content == 'content1'
        assert repo.get_blog_post(1).author == 'author1'
        
        assert repo.get_blog_post(2) is None
        
    def test_get_all_blog_posts(self):
        post = BlogPostCreate(
            title='post1',   
            content='content1',
            author='author1'
        )
        post2 = BlogPostCreate(
            title='post2',   
            content='content2',
            author='author2'
        )
        repo = BlogPostRepository()
        repo.create_blog_post(post)
        repo.create_blog_post(post2)
        
        assert len(repo.get_all_blog_posts()) == 2
        assert repo.get_all_blog_posts()[0].title == 'post1'
        assert repo.get_all_blog_posts()[0].content == 'content1'
        assert repo.get_all_blog_posts()[0].author == 'author1'
        assert repo.get_all_blog_posts()[1].title == 'post2'
        assert repo.get_all_blog_posts()[1].content == 'content2'
        assert repo.get_all_blog_posts()[1].author == 'author2'
        
    def test_get_all_blog_posts_empty(self):
        repo = BlogPostRepository()
        assert len(repo.get_all_blog_posts()) == 0
        
    def test_get_blog_post_not_found(self):
        repo = BlogPostRepository()
        assert repo.get_blog_post(1) is None
        
    def test_delete_blog_post_not_found(self):
        repo = BlogPostRepository()
        assert repo.delete_blog_post(1) is None