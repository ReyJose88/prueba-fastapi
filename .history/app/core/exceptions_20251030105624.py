class AppException(Exception):
    pass

class UnauthorizedActionError(AppException):
    pass

class DatabaseReadError(AppException):
    pass