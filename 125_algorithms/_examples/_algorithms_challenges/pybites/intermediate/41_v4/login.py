import functools

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user, *_ = args
        if user.lower() in known_users:
            if user.lower() in loggedin_users:
                return func(*args, **kwargs)
            else:
                return "please login"
        else:
            return "please create an account"
    return wrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f"welcome back {user}"
