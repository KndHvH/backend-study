from typing import Dict, List, Optional
from models.blog_post import BlogPost

db: Dict[int, BlogPost] = {}

class BlogPostService():
    def __init__(self) -> None:
        pass
    
    def create_blog_post(blog_post:BlogPost) -> BlogPost:
        db[blog_post.post_id] = blog_post
        return blog_post
    
    def delete_blog_post(post_id:int) -> int:
        db.pop(post_id) 
        return post_id
    
    def get_blog_post(post_id:int) -> Optional[BlogPost]:
        return db.get(post_id, None)
    
    def get_all_blog_posts() -> List[BlogPost]:
        return list(db.values())