known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']
from functools import wraps


___ login_required(func):


    @wraps(func)
    ___ wrapper(user):
        __ user  not in known_users:
            return "please create an account"
        __ user not in loggedin_users:
            return "please login"

        return f"welcome back {user}"

    return wrapper

@login_required
___ welcome(user):
    '''Return a welcome message if logged in'''
    pass

