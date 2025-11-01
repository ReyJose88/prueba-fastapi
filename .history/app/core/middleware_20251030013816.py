import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class ResponseTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        process_time = time.time() - start
        print(f"{request.method} {request.url.path} | {process_time:.4f}s")
        return response