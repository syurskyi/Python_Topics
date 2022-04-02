____ functools _______ wraps

known_users =  'bob', 'julian', 'mike', 'carmen', 'sue'
loggedin_users =  'mike', 'sue'


___ login_required(func
    @wraps(func)
    ___ wrapper(args
        #print(args)
        __ args n.. __ known_users:
            r.. 'please create an account'
        ____ args n.. __ loggedin_users:
            r.. 'please login'
        ____:
            r.. func(args)
    r.. wrapper


@login_required
___ welcome(user
    '''Return a welcome message if logged in'''
    r.. f'welcome back {user}'

print(welcome('sue'))