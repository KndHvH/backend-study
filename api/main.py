from fastapi import FastAPI

from api.errors.blog_post_handlers import setup_error_handlers
from api.routes import blog_post_routes, root
from core.middleware.http_logger import log_request_data

app = FastAPI()

app.include_router(root.router)
app.include_router(blog_post_routes.router)

setup_error_handlers(app)

app.middleware("http")(log_request_data)