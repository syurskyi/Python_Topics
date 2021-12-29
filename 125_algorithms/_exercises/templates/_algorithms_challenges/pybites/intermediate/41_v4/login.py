import functools

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


___ login_required(func):
    @functools.wraps(func)
    ___ wrapper(*args, **kwargs):
        user, *_ = args
        __ user.lower() in known_users:
            __ user.lower() in loggedin_users:
                return func(*args, **kwargs)
            else:
                return "please login"
        else:
            return "please create an account"
    return wrapper


@login_required
___ welcome(user):
    '''Return a welcome message if logged in'''
    return f"welcome back {user}"
