____ functools _______ wraps

known_users =  'bob', 'julian', 'mike', 'carmen', 'sue'
loggedin_users =  'mike', 'sue'


___ login_required(func
    @wraps(func)
    ___ wrapped(user
        __ user n.. __ known_users:
            r.. 'please create an account'
        __ user n.. __ loggedin_users:
            r.. 'please login'
        r.. func(user)

    r.. wrapped


@login_required
___ welcome(user
    '''Return a welcome message if logged in'''
    r.. f'welcome back {user}'
