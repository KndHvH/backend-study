
from api.models.blog_post_models import BlogPost, BlogPostCreate, BlogPostPatch, BlogPostUpdate
from api.repository.blog_post_repository import BlogPostRepository


class BlogPostService:
    def __init__(self) -> None:
        self.repository = BlogPostRepository()
    
    def create_blog_post(self, blog_post:BlogPostCreate) -> BlogPost:       
        return self.repository.create_blog_post(blog_post)
    
    def update_blog_post(self, post_id:int, blog_post:BlogPostUpdate) -> BlogPost:
        return self.repository.update_blog_post(post_id, blog_post)
    
    def patch_blog_post(self, post_id:int, blog_post:BlogPostPatch) -> BlogPost:
        return self.repository.patch_blog_post(post_id, blog_post)
        
    def delete_blog_post(self, post_id:int) -> int:
        return self.repository.delete_blog_post(post_id)
    
    def get_blog_post(self, post_id:int) -> BlogPost | None:
        return self.repository.get_blog_post(post_id)
    
    def get_all_blog_posts(self) -> list[BlogPost]:
        return self.repository.get_all_blog_posts()