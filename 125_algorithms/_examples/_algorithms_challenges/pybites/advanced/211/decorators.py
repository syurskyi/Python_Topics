from functools import wraps
import sys

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    @wraps(func)
    def wrapper(*args, **kwargs):
        retries = 0
        while retries < MAX_RETRIES:
            try:
                vals = func(*args, **kwargs)
                break
            except Exception as e:
                retries += 1
                print(e)
        else:
            raise MaxRetriesException

        return vals

    return wrapper
