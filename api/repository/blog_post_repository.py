from datetime import datetime

from api.errors.blog_post_errors import PostNotFoundError
from api.models.blog_post_models import BlogPost, BlogPostCreate, BlogPostPatch, BlogPostUpdate


class BlogPostRepository:
    def __init__(self) -> None:
        self.db: dict[int, BlogPost] = {}
        
    def _get_next_id(self) -> int:
        return max(list(self.db.keys())) + 1 if self.db != {} else 1
    
    def _get_current_datetime(self) -> datetime:
        return datetime.now(datetime.utc)
    
    def create_blog_post(self, blog_post: BlogPostCreate) -> BlogPost:   
        blog_post = BlogPost(
            post_id=self._get_next_id(),
            title=blog_post.title,
            content=blog_post.content,
            author=blog_post.author,
            created_at=self._get_current_datetime(),
            updated_at=self._get_current_datetime()
        )        
        self.db[blog_post.post_id] = blog_post
        return blog_post
    
    def update_blog_post(self, post_id:int, blog_post:BlogPostUpdate) -> BlogPost:
        if post_id not in self.db:
            raise PostNotFoundError(post_id)
        
        blog_post = BlogPost(
            post_id=post_id,
            title=blog_post.title,
            content=blog_post.content,
            author=blog_post.author,
            created_at=self.db[post_id].created_at,
            updated_at=self._get_current_datetime()
        )
        
        self.db[post_id] = blog_post
        return blog_post
    
    def patch_blog_post(self, post_id:int, blog_post:BlogPostPatch) -> BlogPost:
        if post_id not in self.db:
            raise PostNotFoundError(post_id)
        
        self.db[post_id].updated_at = self._get_current_datetime()
        
        if blog_post.title is not None:
            self.db[post_id].title = blog_post.title
            
        if blog_post.author is not None:
            self.db[post_id].author = blog_post.author
            
        if blog_post.content is not None:
            self.db[post_id].content = blog_post.content
        
        return self.db[post_id]
    
    def delete_blog_post(self, post_id:int) -> int:
        if post_id not in self.db:
            raise PostNotFoundError(post_id)
        
        self.db.pop(post_id)
        return post_id
    
    def get_blog_post(self, post_id:int) -> BlogPost | None:
        if post_id not in self.db:
            raise PostNotFoundError(post_id)
        return self.db[post_id]
    
    def get_all_blog_posts(self) -> list[BlogPost]:
        return list(self.db.values())