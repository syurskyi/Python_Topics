from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def wrapper(args):
        #print(args)
        if args not in known_users:
            return 'please create an account'
        elif args not in loggedin_users:
            return 'please login'
        else:
            return func(args)
    return wrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'

print(welcome('sue'))