____ functools _______ wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


___ login_required(func):
    @wraps(func)
    ___ wrapper(*args):
        __ args[0] __ loggedin_users:
            r.. func(args[0])

        __ args[0] __ known_users and args[0] n.. __ loggedin_users:
            r.. "please login"

        __ args[0] n.. __ known_users and args[0] n.. __ loggedin_users:
            r.. "please create an account"
    r.. wrapper


@login_required
___ welcome(user):
    '''Return a welcome message if logged in'''
    r.. f"welcome back {user}"

# if __name__ == "__main__":
#     welcome("bob")