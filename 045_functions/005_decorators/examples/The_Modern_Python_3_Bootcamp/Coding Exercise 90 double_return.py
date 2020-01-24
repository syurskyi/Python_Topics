# Double Return Decorator
#
# Most of this function is decorator boilerplate...

from functools import wraps

"""
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # logic goes in here...
    return wrapper
"""

# This wrapper function simply runs the function, and returns a list containing the result twice:

from functools import wraps


def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

