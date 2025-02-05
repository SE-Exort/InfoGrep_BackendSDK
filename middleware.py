from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from .infogrep_logger.logger import Logger

class TracingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        for k, v in request.headers.items():
            if k.startswith("x-") or k.startswith("trace"):
                response.headers[k] = v
        return response

class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, logger: Logger): 
        self.logger = logger
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next):
        self.logger.info(msg=f"Request sent by {request.client.host} to {request.url} started")
        
        response = await call_next(request)
        status_code = str(response.status_code)
        if status_code.startswith('4') or status_code.startswith('5'):
            self.logger.error(
                msg=f"ERROR: Request sent by {request.client.host} to {request.url} failed",
                extra={
                    "status_code": status_code,
                    "content": response.body()
                })
        elif status_code == "200":
            self.logger.info(
                msg=f"Request sent by {request.client.host} to {request.url} completed",
                extra={
                    "status_code": status_code,
                })

        return response
