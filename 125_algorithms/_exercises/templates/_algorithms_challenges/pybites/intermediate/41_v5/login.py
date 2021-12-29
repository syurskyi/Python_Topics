from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


___ login_required(func):
    @wraps(func)
    ___ wrapped(user):
        __ user not in known_users:
            return 'please create an account'
        __ user not in loggedin_users:
            return 'please login'
        return func(user)

    return wrapped


@login_required
___ welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'
