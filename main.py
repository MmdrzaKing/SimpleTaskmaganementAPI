from datetime import datetime, timezone

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from exceptions.exceptions import AppException
from routes.routes import router as task_router
from responses.responses import build_error_response

app = FastAPI()

app.include_router(task_router)


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
            "error": {
                "code": exc.code
            },
            "meta": {
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error",
            "error": {
                "code": "INTERNAL_SERVER_ERROR"
            },
            "meta": {
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content=build_error_response(
            message="Validation failed",
            code="VALIDATION_ERROR",
            details=exc.errors()
        )
    )


@app.get("/")
def status_check():
    return {"status": "Running"}