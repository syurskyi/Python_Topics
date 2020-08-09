from functools ______ wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


___ login_required(func
    @wraps(func)
    ___ wrapped(user
        __ user not in known_users:
            r_ 'please create an account'
        __ user not in loggedin_users:
            r_ 'please login'
        r_ func(user)

    r_ wrapped


@login_required
___ welcome(user
    '''Return a welcome message if logged in'''
    r_ f'welcome back {user}'
