from functools import wraps


___ int_args(func):
    @wraps(func)
    ___ wrapper(*args):
        # Validate arg type and value
        for arg in args:
            __ not isinstance(arg, int):
                raise TypeError
            else:
                __ arg < 0:
                    raise ValueError
        return func(*args)
    return wrapper