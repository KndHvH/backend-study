from fastapi import APIRouter
from api.models.blog_post_models import BlogPostCreate, BlogPostUpdate, BlogPostPatch
from api.services.blog_post_services import BlogPostService


router = APIRouter()
blog_post_service = BlogPostService()

@router.post("/blog_posts", status_code=201)
def create_blog_post(blog_post: BlogPostCreate):
    return blog_post_service.create_blog_post(blog_post)

@router.put("/blog_posts/{post_id}", status_code=200)
def update_blog_post(post_id: int, blog_post: BlogPostUpdate):
    return blog_post_service.update_blog_post(post_id, blog_post)

@router.patch("/blog_posts/{post_id}", status_code=200)
def patch_blog_post(post_id: int, blog_post: BlogPostPatch):
    return blog_post_service.patch_blog_post(post_id, blog_post)

@router.delete("/blog_posts/{post_id}", status_code=204)
def delete_blog_post(post_id: int):
    blog_post_service.delete_blog_post(post_id)

@router.get("/blog_posts/{post_id}", status_code=200)
def get_blog_post(post_id: int):
    return blog_post_service.get_blog_post(post_id)
    
@router.get("/blog_posts", status_code=200)
def get_all_blog_posts():
    return blog_post_service.get_all_blog_posts()
