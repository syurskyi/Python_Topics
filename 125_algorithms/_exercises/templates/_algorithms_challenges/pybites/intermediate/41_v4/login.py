_______ functools

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


___ login_required(func):
    @functools.wraps(func)
    ___ wrapper(*args, **kwargs):
        user, *_ = args
        __ user.lower() __ known_users:
            __ user.lower() __ loggedin_users:
                r.. func(*args, **kwargs)
            ____:
                r.. "please login"
        ____:
            r.. "please create an account"
    r.. wrapper


@login_required
___ welcome(user):
    '''Return a welcome message if logged in'''
    r.. f"welcome back {user}"
