from datetime import datetime
from typing import Dict, List, Optional
from api.models.blog_post_models import BlogPost, BlogPostCreate, BlogPostUpdate, BlogPostPatch
from api.errors.blog_post_errors import PostAlreadyExists, PostNotFoundError

db: Dict[int, BlogPost] = {}

class BlogPostService():
    def __init__(self) -> None:
        pass
    
    def create_blog_post(self, blog_post:BlogPostCreate) -> BlogPost:       
        next_id = max(list(db.keys())) + 1 if db != {} else 1
        current_datetime = datetime.now()
        
        blog_post = BlogPost(
            post_id=next_id,
            title=blog_post.title,
            content=blog_post.content,
            author=blog_post.author,
            created_at=current_datetime,
            updated_at=current_datetime
        )        
        db[blog_post.post_id] = blog_post
        return blog_post
    
    def update_blog_post(self, post_id:int, blog_post:BlogPostUpdate) -> BlogPost:
        if post_id not in db:
            raise PostNotFoundError(post_id)
        
        current_datetime = datetime.now()
        
        blog_post = BlogPost(
            post_id=post_id,
            title=blog_post.title,
            content=blog_post.content,
            author=blog_post.author,
            created_at=db[post_id].created_at,
            updated_at=current_datetime
        )
        
        db[post_id] = blog_post
        return blog_post
    
    def patch_blog_post(self, post_id:int, blog_post:BlogPostPatch) -> BlogPost:
        if post_id not in db:
            raise PostNotFoundError(post_id)
        
        db[post_id].updated_at = datetime.now()
        
        if blog_post.title is not None:
            db[post_id].title = blog_post.title
            
        if blog_post.author is not None:
            db[post_id].author = blog_post.author
            
        if blog_post.content is not None:
            db[post_id].content = blog_post.content
        
        return db[post_id]
        
    def delete_blog_post(self, post_id:int) -> int:
        if post_id not in db:
            raise PostNotFoundError(post_id)
        db.pop(post_id) 
        return post_id
    
    def get_blog_post(self, post_id:int) -> Optional[BlogPost]:
        if post_id not in db:
            raise PostNotFoundError(post_id)
        return db.get(post_id, None)
    
    def get_all_blog_posts(self) -> List[BlogPost]:
        return list(db.values())