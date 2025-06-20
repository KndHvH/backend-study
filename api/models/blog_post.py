from pydantic import BaseModel
from datetime import datetime   

class BlogPost(BaseModel):
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
    title: str
    content: str
    author: str
    created_at: datetime