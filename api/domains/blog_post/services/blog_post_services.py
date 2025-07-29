
from api.domains.blog_post.interfaces.blog_post_interface import IBlogPostRepository
from api.domains.blog_post.models.blog_post_models import BlogPost, BlogPostCreate, BlogPostPatch, BlogPostUpdate
from core.logger import app_logger


class BlogPostService:
    def __init__(self, repository: IBlogPostRepository) -> None:
        self.repository = repository
    
    def create_blog_post(self, blog_post:BlogPostCreate) -> BlogPost:       
        post = self.repository.create_blog_post(blog_post)
        app_logger.debug(f"Blog post created: id={post.post_id}, title='{post.title}', author='{post.author}'")
        app_logger.debug(f"Blog post created: {post.model_dump_json()}")
        return post
    
    def update_blog_post(self, post_id:int, blog_post:BlogPostUpdate) -> BlogPost:
        post = self.repository.update_blog_post(post_id, blog_post)
        app_logger.debug(f"Blog post updated: id={post.post_id}, title='{post.title}', author='{post.author}'")
        app_logger.debug(f"Blog post updated: {post.model_dump_json()}")
        return post
    
    def patch_blog_post(self, post_id:int, blog_post:BlogPostPatch) -> BlogPost:
        post = self.repository.patch_blog_post(post_id, blog_post)
        app_logger.debug(f"Blog post patched: id={post.post_id}, title='{post.title}', author='{post.author}'")
        app_logger.debug(f"Blog post patched: {post.model_dump_json()}")
        return post
        
    def delete_blog_post(self, post_id:int) -> int:
        self.repository.delete_blog_post(post_id)
        app_logger.debug(f"Blog post deleted: id={post_id}")
        app_logger.debug(f"Blog post deleted: id={post_id}")
        return post_id
    
    def get_blog_post(self, post_id:int) -> BlogPost | None:
        post = self.repository.get_blog_post(post_id)
        app_logger.debug(f"Blog post retrieved: id={post.post_id}, title='{post.title}', author='{post.author}'")
        app_logger.debug(f"Blog post retrieved: {post.model_dump_json()}")
        return post
    
    def get_all_blog_posts(self) -> list[BlogPost]:
        posts = self.repository.get_all_blog_posts()
        app_logger.debug(f"All blog posts retrieved: {len(posts)} posts")
        return posts