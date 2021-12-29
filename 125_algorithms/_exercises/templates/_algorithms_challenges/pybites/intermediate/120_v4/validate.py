____ functools _______ wraps


___ int_args(func):
    @wraps(func)
    ___ wrapper(*args, **kwargs):
        __ n.. a..(map(l.... x: isi..(x, int), args)):
            raise TypeError
        ____ any(map(l.... x: x < 0, args)):
            raise ValueError
        r.. func(*args, **kwargs)
    r.. wrapper
#
