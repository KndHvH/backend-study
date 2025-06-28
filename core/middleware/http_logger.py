from time import perf_counter
from fastapi import Request
from core.logger import app_logger

async def log_request_data(request: Request, call_next):
    start = perf_counter()

    response = await call_next(request)
    duration = perf_counter() - start

    ip = request.client.host or "unknown"
    method = request.method
    path = request.url.path
    status = response.status_code
    
    app_logger.info(
		f"{ip} - {method} {path} → {status} | {duration:.2f}s"
	)

    return response
