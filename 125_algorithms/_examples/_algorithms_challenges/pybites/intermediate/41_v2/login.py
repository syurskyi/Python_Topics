known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']
from functools import wraps


def login_required(func):


    @wraps(func)
    def wrapper(user):
        if user  not in known_users:
            return "please create an account"
        if user not in loggedin_users:
            return "please login"

        return f"welcome back {user}"

    return wrapper

@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    pass

