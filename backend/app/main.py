from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.routes import error_routes
from app.services.logger_service import log_error
from datetime import datetime

app = FastAPI(title="Error Tracking System")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ErrorLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            # Capture 4xx and 5xx errors
            if 400 <= response.status_code < 600:
                error_data = {
                    "api_name": request.url.path,
                    "status_code": response.status_code,
                    "error_message": "HTTP Error", 
                    "timestamp": datetime.utcnow(),
                    "is_critical": response.status_code >= 500
                }
                # Log asynchronously (in a real app, use BackgroundTasks)
                # For interview simplicity, direct call is acceptable or use BackgroundTasks if preferred
                log_error(error_data)
            return response
        except Exception as exc:
            # Capture unhandled exceptions (Critical 500)
            error_data = {
                "api_name": request.url.path,
                "status_code": 500,
                "error_message": str(exc),
                "timestamp": datetime.utcnow(),
                "is_critical": True
            }
            log_error(error_data)
            raise exc

app.add_middleware(ErrorLoggingMiddleware)

app.include_router(error_routes.router)

@app.get("/")
def root():
    return {"message": "Error Tracking System Active"}
