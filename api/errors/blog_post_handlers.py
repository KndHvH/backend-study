from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from api.errors.blog_post_errors import PostError
from core.logger import app_logger


def setup_error_handlers(app: FastAPI):
    app.add_exception_handler(PostError, post_error_handler)
    app.add_exception_handler(RequestValidationError, validation_error_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)

async def post_error_handler(request: Request, exc: PostError):
    app_logger.warning(f"Post error at {request.url.path}: {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.as_response()
    )
    
async def validation_error_handler(request: Request, exc: RequestValidationError):
    app_logger.warning(f"Validation error at {request.url.path}: {str(exc.errors())}")
    return JSONResponse(
        status_code=422,
        content={"detail": str(exc.errors())},
    )
    
    
async def unhandled_exception_handler(request: Request, exc: Exception):
    app_logger.exception(f"Unhandled exception at {request.url.path}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )
