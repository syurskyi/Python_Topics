from functools import wraps


___ int_args(func):
    @wraps(func)
    ___ wrapper(*args, **kwargs):
        for a in args:
            __ not isinstance(a, int):
                raise TypeError()
            __ a < 0:
                raise ValueError()
        return func(*args, **kwargs)

    return wrapper
