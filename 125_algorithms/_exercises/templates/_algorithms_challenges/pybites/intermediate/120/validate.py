____ functools _______ wraps


___ int_args(func):
    @wraps(func)
    ___ wrapper(*args):
        # Validate arg type and value
        ___ arg __ args:
            __ n.. isi..(arg, int):
                raise TypeError
            ____:
                __ arg < 0:
                    raise ValueError
        r.. func(*args)
    r.. wrapper