from typing import Optional
from datetime import datetime
from itertools import combinations
from pydantic import BaseModel, field_validator, model_validator


class BlogPostBaseModel(BaseModel):
    """
    Blog post base model
    Attributes:
        title: str
        content: str
        author: str
    """
    title: str
    content: str
    author: str
    
    @field_validator('title', 'content', 'author')
    @classmethod
    def validate_fields(cls, value: str | None) -> str:
        if value is None:
            return value
        if len(value) < 3 or len(value) > 100 or not value.strip(): 
            raise ValueError(f"Field must be a non-empty string between 3 and 100 characters")
        return value
    
    @model_validator(mode='after')
    def validate_model(self):
        
        fields = {
            "title": self.title,
            "content": self.content,
            "author": self.author
        }
        
        for (name1, val1), (name2, val2) in combinations(fields.items(), 2):
            if val1 is not None and val2 is not None and val1 == val2:
                raise ValueError(f"{name1.capitalize()} and {name2.capitalize()} cannot be the same")
        return self

class BlogPost(BlogPostBaseModel):
    """
    Blog post model
    Attributes:
        post_id: int
        title: str
        content: str
        author: str
        created_at: datetime
        updated_at: datetime
        
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
        title: Optional[str]
        content: Optional[str]
        author: Optional[str]

    """
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
