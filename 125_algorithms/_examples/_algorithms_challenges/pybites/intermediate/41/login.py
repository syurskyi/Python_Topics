from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def wrapper(*args):
        if args[0] in loggedin_users:
            return func(args[0])

        if args[0] in known_users and args[0] not in loggedin_users:
            return "please login"

        if args[0] not in known_users and args[0] not in loggedin_users:
            return "please create an account"
    return wrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f"welcome back {user}"

# if __name__ == "__main__":
#     welcome("bob")