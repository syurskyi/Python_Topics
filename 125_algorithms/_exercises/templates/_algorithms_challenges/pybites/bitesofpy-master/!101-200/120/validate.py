from functools ______ wraps


___ int_args(func
    @wraps(func)
    ___ wrapper(*args, **kwargs
        ___ a __ args:
            __ not isinstance(a, int
                raise TypeError()
            __ a < 0:
                raise ValueError()
        r_ func(*args, **kwargs)

    r_ wrapper
