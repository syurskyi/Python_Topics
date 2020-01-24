# Show Args Decorator Solution
#
# ignoring all the boilerplate code (the stuff that goes in every decorator function, wraps,e tc.),
# the important logic is really just:

"""
print("Here are the args:", args)
print("Here are the kwargs:", kwargs)
return fn(*args, **kwargs)
"""

# Here's the complete code:

from functools import wraps


def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)

    return wrapper