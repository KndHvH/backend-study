from fastapi import APIRouter

from api.models.blog_post_models import BlogPostCreate, BlogPostPatch, BlogPostUpdate, BlogPost
from api.models.response_models import ResponseModel
from api.services.blog_post_services import BlogPostService
from core.logger import app_logger

router = APIRouter()
blog_post_service = BlogPostService()

@app_logger.catch(level="ERROR")
@router.post("/blog_posts", status_code=201, response_model=ResponseModel[BlogPost])
def create_blog_post(blog_post: BlogPostCreate):
    return ResponseModel(
        success=True, 
        message="Blog post created successfully", 
        data=blog_post_service.create_blog_post(blog_post)
    )

@app_logger.catch(level="ERROR")
@router.put("/blog_posts/{post_id}", status_code=200, response_model=ResponseModel[BlogPost])
def update_blog_post(post_id: int, blog_post: BlogPostUpdate):
    return ResponseModel(
        success=True, 
        message="Blog post updated successfully", 
        data=blog_post_service.update_blog_post(post_id, blog_post)
    )

@app_logger.catch(level="ERROR")
@router.patch("/blog_posts/{post_id}", status_code=200, response_model=ResponseModel[BlogPost])
def patch_blog_post(post_id: int, blog_post: BlogPostPatch):
    return ResponseModel(
        success=True, 
        message="Blog post patched successfully", 
        data=blog_post_service.patch_blog_post(post_id, blog_post)
    )

@app_logger.catch(level="ERROR")
@router.delete("/blog_posts/{post_id}", status_code=204)
def delete_blog_post(post_id: int):
    blog_post_service.delete_blog_post(post_id)

@app_logger.catch(level="ERROR")
@router.get("/blog_posts/{post_id}", status_code=200, response_model=ResponseModel[BlogPost])
def get_blog_post(post_id: int):
    return ResponseModel(
        success=True, 
        message="Blog post retrieved successfully", 
        data=blog_post_service.get_blog_post(post_id)
    )
    
@app_logger.catch(level="ERROR")
@router.get("/blog_posts", status_code=200, response_model=ResponseModel[list[BlogPost]])
def get_all_blog_posts():
    return ResponseModel(
        success=True, 
        message="All blog posts retrieved successfully", 
        data=blog_post_service.get_all_blog_posts()
    )
