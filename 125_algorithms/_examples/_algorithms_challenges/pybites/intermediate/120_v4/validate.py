from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not all(map(lambda x: isinstance(x, int), args)):
            raise TypeError
        elif any(map(lambda x: x < 0, args)):
            raise ValueError
        return func(*args, **kwargs)
    return wrapper
#
