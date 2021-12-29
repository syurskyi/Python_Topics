from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args):
        # Validate arg type and value
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError
            else:
                if arg < 0:
                    raise ValueError
        return func(*args)
    return wrapper