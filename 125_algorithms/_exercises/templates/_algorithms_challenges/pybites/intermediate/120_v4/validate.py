from functools import wraps


___ int_args(func):
    @wraps(func)
    ___ wrapper(*args, **kwargs):
        __ not all(map(lambda x: isinstance(x, int), args)):
            raise TypeError
        elif any(map(lambda x: x < 0, args)):
            raise ValueError
        return func(*args, **kwargs)
    return wrapper
#
