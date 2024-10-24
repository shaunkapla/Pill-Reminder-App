class UserAlreadyExistsError(Exception):
    """
    This is an exception to catch if a user exists already
    """
    pass

class UserDoesntExistError(Exception):
    """
    This is an exception to catch if a user doesn't exist
    """
    pass