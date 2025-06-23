from typing import Optional
from pydantic import BaseModel
from datetime import datetime   


class BlogPostBaseModel(BaseModel):
    """
    Blog post model
    Attributes:
        post_id: int
        title: str
        content: str
        author: str
        created_at: datetime
    """
    title: str
    content: str
    author: str

class BlogPost(BlogPostBaseModel):
    """
    Blog post model
    Attributes:
        post_id: int
        title: str
        content: str
        author: str
        created_at: datetime
    """
    post_id: int 
    created_at: datetime
    updated_at: datetime
    
class BlogPostCreate(BlogPostBaseModel):
    """
    Blog post create model
    Attributes:
        title: str
        content: str
        author: str
    """
    pass
    

class BlogPostUpdate(BlogPostBaseModel):
    """
    Blog post update model
    Attributes:
        title: str
        content: str
        author: str
    """
    pass
    
class BlogPostPatch(BlogPostBaseModel):
    """
    Blog post patch model
    Attributes:
        title: str
        content: str
        author: str
    """
    title: Optional[str]
    content: Optional[str]
    author: Optional[str]
