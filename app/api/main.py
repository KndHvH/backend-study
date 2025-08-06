from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.domains.blog_post.errors.blog_post_handlers import setup_error_handlers
from app.api.domains.blog_post.routes import blog_post_routes, root
from app.core.database.make_db import make_db
from app.core.middleware.http_logger import log_request_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    make_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(root.router)
app.include_router(blog_post_routes.router)

setup_error_handlers(app)

app.middleware("http")(log_request_data)
