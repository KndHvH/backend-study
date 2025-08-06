from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.domains.blog_post.models.blog_post_models import BlogPost, BlogPostCreate, BlogPostPatch, BlogPostUpdate
from app.api.domains.blog_post.models.response_models import ResponseModel
from app.api.domains.blog_post.repository.blog_post_repository import BlogPostRepository
from app.api.domains.blog_post.services.blog_post_services import BlogPostService
from app.core.database.db import get_db
from app.core.logger import app_logger

router = APIRouter()


@app_logger.catch(level="ERROR")
@router.post("/blog_posts", status_code=201, response_model=ResponseModel[BlogPost])
def create_blog_post(blog_post: BlogPostCreate, session: Annotated[Session, Depends(get_db)]):
    repository = BlogPostRepository(session=session)
    service = BlogPostService(repository=repository)
    return ResponseModel(
        success=True, 
        message="Blog post created successfully", 
        data=service.create_blog_post(blog_post)
    )

@app_logger.catch(level="ERROR")
@router.put("/blog_posts/{post_id}", status_code=200, response_model=ResponseModel[BlogPost])
def update_blog_post(post_id: int, blog_post: BlogPostUpdate, session: Annotated[Session, Depends(get_db)]):
    repository = BlogPostRepository(session=session)
    service = BlogPostService(repository=repository)
    return ResponseModel(
        success=True, 
        message="Blog post updated successfully", 
        data=service.update_blog_post(post_id, blog_post)
    )

@app_logger.catch(level="ERROR")
@router.patch("/blog_posts/{post_id}", status_code=200, response_model=ResponseModel[BlogPost])
def patch_blog_post(post_id: int, blog_post: BlogPostPatch, session: Annotated[Session, Depends(get_db)]):
    repository = BlogPostRepository(session=session)
    service = BlogPostService(repository=repository)
    return ResponseModel(
        success=True, 
        message="Blog post patched successfully", 
        data=service.patch_blog_post(post_id, blog_post)
    )

@app_logger.catch(level="ERROR")
@router.delete("/blog_posts/{post_id}", status_code=204)
def delete_blog_post(post_id: int, session: Annotated[Session, Depends(get_db)]):
    repository = BlogPostRepository(session=session)
    service = BlogPostService(repository=repository)
    service.delete_blog_post(post_id)

@app_logger.catch(level="ERROR")
@router.get("/blog_posts/{post_id}", status_code=200, response_model=ResponseModel[BlogPost])
def get_blog_post(post_id: int, session: Annotated[Session, Depends(get_db)]):
    repository = BlogPostRepository(session=session)
    service = BlogPostService(repository=repository)
    return ResponseModel(
        success=True, 
        message="Blog post retrieved successfully", 
        data=service.get_blog_post(post_id)
    )
    
@app_logger.catch(level="ERROR")
@router.get("/blog_posts", status_code=200, response_model=ResponseModel[list[BlogPost]])
def get_all_blog_posts(session: Annotated[Session, Depends(get_db)]):
    repository = BlogPostRepository(session=session)
    service = BlogPostService(repository=repository)
    return ResponseModel(
        success=True, 
        message="All blog posts retrieved successfully", 
        data=service.get_all_blog_posts()
    )
