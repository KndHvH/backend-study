from typing import Dict, List, Optional
from api.models.blog_post_models import BlogPost
from api.errors.blog_post_errors import PostAlreadyExists, PostNotFoundError

db: Dict[int, BlogPost] = {}

class BlogPostService():
    def __init__(self) -> None:
        pass
    
    def create_blog_post(self, blog_post:BlogPost) -> BlogPost:
        if blog_post.post_id in db:
            raise PostAlreadyExists(blog_post.post_id)
        db[blog_post.post_id] = blog_post
        return blog_post
    
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