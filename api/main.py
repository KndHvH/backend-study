from fastapi import FastAPI

from api.errors.blog_post_errors import PostError
from api.errors.blog_post_handlers import post_error_handler
from api.routes import blog_post_routes, root

app = FastAPI()

app.include_router(root.router)
app.include_router(blog_post_routes.router)

app.add_exception_handler(PostError, post_error_handler)