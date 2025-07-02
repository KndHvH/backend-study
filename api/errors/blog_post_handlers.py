from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from api.errors.blog_post_errors import PostError
from api.models.response_models import ResponseModel
from core.logger import app_logger


def setup_error_handlers(app: FastAPI):
    app.add_exception_handler(PostError, post_error_handler)
    app.add_exception_handler(RequestValidationError, validation_error_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)

async def post_error_handler(request: Request, exc: PostError):
    app_logger.warning(f"Post error at {request.url.path}: '{exc.message}'")
    content = ResponseModel(
        success=False,
        message=exc.message,
        data=None
    )
    return JSONResponse(
        status_code=400,
        content=content.model_dump()
    )
    
async def validation_error_handler(request: Request, exc: RequestValidationError):
    error_msg = str(exc.errors()[0]["msg"]) if exc.errors() else "Validation error"
    app_logger.warning(f"Validation error at {request.url.path}: '{error_msg}'")
    content = ResponseModel(
        success=False,
        message=error_msg,
        data=None
    )
    return JSONResponse(
        status_code=422,
        content=content.model_dump()
    )
    
    
async def unhandled_exception_handler(request: Request, exc: Exception):
    app_logger.exception(f"Unhandled exception at {request.url.path}: {str(exc)}")
    content = ResponseModel(
        success=False,
        message="Internal Server Error",
        data=None
    )
    return JSONResponse(
        status_code=500,
        content=content.model_dump()
    )
