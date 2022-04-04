known_users =  'bob', 'julian', 'mike', 'carmen', 'sue' 
loggedin_users =  'mike', 'sue' 
____ f.. _______ wraps


___ login_required(func


    @wraps(func)
    ___ wrapper(user
        __ user  n.. __ known_users:
            r.. "please create an account"
        __ user n.. __ loggedin_users:
            r.. "please login"

        r.. f"welcome back {user}"

    r.. wrapper

@login_required
___ welcome(user
    '''Return a welcome message if logged in'''
    p..

