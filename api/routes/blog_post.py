from fastapi import APIRouter
from models.blog_post import BlogPost
from services.blog_post import BlogPostService

router = APIRouter()

@router.post("/blog_posts")
def create_blog_post(blog_post: BlogPost):
    return BlogPostService.create_blog_post(blog_post)

@router.delete("/blog_posts/{post_id}")
def delete_blog_post(post_id: int):
    return BlogPostService.delete_blog_post(post_id)

@router.get("/blog_posts/{post_id}")
def get_blog_post(post_id: int):
    return BlogPostService.get_blog_post(post_id)