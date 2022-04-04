_______ f..

known_users =  'bob', 'julian', 'mike', 'carmen', 'sue'
loggedin_users =  'mike', 'sue'


___ login_required(func
    @f...wraps(func)
    ___ wrapper $ $$:
        user, *_ = args
        __ user.l.. __ known_users:
            __ user.l.. __ loggedin_users:
                r.. func $ $$
            ____
                r.. "please login"
        ____
            r.. "please create an account"
    r.. wrapper


@login_required
___ welcome(user
    '''Return a welcome message if logged in'''
    r.. f"welcome back {user}"
