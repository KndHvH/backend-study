import uuid
from time import perf_counter

from fastapi import Request

from core.logger import app_logger
from core.settings import settings


async def log_request_data(request: Request, call_next):
    start = perf_counter()
    request_id = str(uuid.uuid4())

    response = await call_next(request)
    duration = perf_counter() - start
    
    response.headers["X-Response-Time"] = f"{duration:.3f}s"
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Env"] = settings.environment

    ip = request.client.host or "unknown"
    method = request.method
    path = request.url.path
    status = response.status_code
    
    message = f"{ip:12} {method:6} {path:24} → {status:3} | {duration:4.2f}s | [ID:{request_id}] | "

    app_logger.info(message)

    return response
