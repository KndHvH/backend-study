from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.domains.blog_post.models.blog_post_models import BlogPost, BlogPostCreate, BlogPostPatch, BlogPostUpdate
from api.domains.blog_post.models.response_models import ResponseModel
from api.domains.blog_post.services.blog_post_services import BlogPostService
from core.database.db import get_db
from core.logger import app_logger

router = APIRouter()

@app_logger.catch(level="ERROR")
@router.post("/blog_posts", status_code=201, response_model=ResponseModel[BlogPost])
def create_blog_post(blog_post: BlogPostCreate, db: Annotated[Session, Depends(get_db)]):
    blog_post_service = BlogPostService(db)
    return ResponseModel(
        success=True, 
        message="Blog post created successfully", 
        data=blog_post_service.create_blog_post(blog_post)
    )

@app_logger.catch(level="ERROR")
@router.put("/blog_posts/{post_id}", status_code=200, response_model=ResponseModel[BlogPost])
def update_blog_post(post_id: int, blog_post: BlogPostUpdate, db: Annotated[Session, Depends(get_db)]):
    blog_post_service = BlogPostService(db)
    return ResponseModel(
        success=True, 
        message="Blog post updated successfully", 
        data=blog_post_service.update_blog_post(post_id, blog_post)
    )

@app_logger.catch(level="ERROR")
@router.patch("/blog_posts/{post_id}", status_code=200, response_model=ResponseModel[BlogPost])
def patch_blog_post(post_id: int, blog_post: BlogPostPatch, db: Annotated[Session, Depends(get_db)]):
    blog_post_service = BlogPostService(db)
    return ResponseModel(
        success=True, 
        message="Blog post patched successfully", 
        data=blog_post_service.patch_blog_post(post_id, blog_post)
    )

@app_logger.catch(level="ERROR")
@router.delete("/blog_posts/{post_id}", status_code=204)
def delete_blog_post(post_id: int, db: Annotated[Session, Depends(get_db)]):
    blog_post_service = BlogPostService(db)
    blog_post_service.delete_blog_post(post_id)

@app_logger.catch(level="ERROR")
@router.get("/blog_posts/{post_id}", status_code=200, response_model=ResponseModel[BlogPost])
def get_blog_post(post_id: int, db: Annotated[Session, Depends(get_db)]):
    blog_post_service = BlogPostService(db)
    return ResponseModel(
        success=True, 
        message="Blog post retrieved successfully", 
        data=blog_post_service.get_blog_post(post_id)
    )
    
@app_logger.catch(level="ERROR")
@router.get("/blog_posts", status_code=200, response_model=ResponseModel[list[BlogPost]])
def get_all_blog_posts(db: Annotated[Session, Depends(get_db)]):
    blog_post_service = BlogPostService(db)
    return ResponseModel(
        success=True, 
        message="All blog posts retrieved successfully", 
        data=blog_post_service.get_all_blog_posts()
    )
