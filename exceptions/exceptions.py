class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400, code: str = "UNKNOWN_ERROR"):
        self.message = message
        self.status_code = status_code
        self.code = code
        super().__init__(self.message)


class NotFoundError(AppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404, code="NOT_FOUND")
        

class ConflictError(AppException):
    def __init__(self, message: str = "Conflict occurred"):
        super().__init__(message, status_code=409, code="CONFLICT_ERROR")

class ValidationError(AppException):
    def __init__(self, message: str = "Validation error"):
        super().__init__(message, status_code=422, code="VALIDATION_ERROR")


class DatabaseError(AppException):
    def __init__(self, message: str = "Database error"):
        super().__init__(message, status_code=500, code="DATABASE_ERROR")


class InternalServerError(AppException):
    def __init__(self, message: str = "Internal server error"):
        super().__init__(message, status_code=500, code="INTERNAL_SERVER_ERROR")