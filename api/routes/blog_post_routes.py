from fastapi import APIRouter
from api.models.blog_post_models import BlogPost
from api.services.blog_post_services import BlogPostService

router = APIRouter()
blog_post_service = BlogPostService()

@router.post("/blog_posts")
def create_blog_post(blog_post: BlogPost):
    return blog_post_service.create_blog_post(blog_post)

@router.delete("/blog_posts/{post_id}")
def delete_blog_post(post_id: int):
    return blog_post_service.delete_blog_post(post_id)

@router.get("/blog_posts/{post_id}")
def get_blog_post(post_id: int):
    return blog_post_service.get_blog_post(post_id)

@router.get("/blog_posts")
def get_all_blog_posts():
    return blog_post_service.get_all_blog_posts()