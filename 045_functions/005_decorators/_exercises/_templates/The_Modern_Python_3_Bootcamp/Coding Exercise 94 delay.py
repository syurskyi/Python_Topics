# Delay Decorator Solution

from functools import wraps
from time import sleep


def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(timer, fn.__name__))
            sleep(timer)
            return fn(*args, **kwargs)

        return wrapper

    return inner

