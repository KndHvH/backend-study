from fastapi import Request
from fastapi.responses import JSONResponse

from api.errors.blog_post_errors import PostError


async def post_error_handler(request: Request, exc: PostError):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.as_response()
    )