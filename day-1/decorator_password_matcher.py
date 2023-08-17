def authenticate(username, password):
    """
    This function is used to authenticate the user
    Args:
        username (_String_): username of user
        password (_String_): password of user

    Returns:
        _bool_: return `true` if username and password is correct otherwise\
        return false
    """
    return username == "admin" and password == "secret"


def isAuthenticated(func):
    """
    isAuthenticated is used to decorate the authenticate_user 

    Args:
        func (_function_): takes argument as function which is to be decorated
    """
    def wrapper(**kwargs):
        """
        Inner wrapper function to authenticate.
        
        Parameters:
        *args: Arguments from the decorated function.
        **kwargs: Keyword arguments from the decorated function.
        
        """
        username = kwargs["username"]
        password = kwargs["password"]
        if authenticate(username=username, password=password):
            print("Access Granted. Congratulation !!!")
        else:
            print("Authentication Failed. Access Denied")
    return wrapper
    
    
@isAuthenticated
def authenticate_user(**kwargs):
    return kwargs
    
    
if __name__ == "__main__":
    authenticate_user(username="admin", password="secret")
    
    