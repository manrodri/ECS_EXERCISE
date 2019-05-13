class Error(Exception):
    "Base class for other exceptions"
    pass

class CreateConnectionException(Error):
    "Raised when there in an error creating connection to DB"
    pass

class SqlSyntaxException(Error):
    "Raised when raw SQL statement produce an exception"
    pass

class LoginDbException(Error):
    "Raised if incorrect credentials are passed"
    pass

