from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


___ login_required(func):
    @wraps(func)
    ___ wrapper(args):
        #print(args)
        __ args not in known_users:
            return 'please create an account'
        elif args not in loggedin_users:
            return 'please login'
        else:
            return func(args)
    return wrapper


@login_required
___ welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'

print(welcome('sue'))