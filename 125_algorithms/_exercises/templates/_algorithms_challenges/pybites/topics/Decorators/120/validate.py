____ functools _______ wraps


___ int_args(func):
    @wraps(func)
    # complete this decorator
    ___ wrapper(*args):
        __ s..(isi..(n, str) ___ n __ args):
            raise TypeError
        ____ s..(isi..(n, float) ___ n __ args):
            raise TypeError
        ____ s..(n < 0 ___ n __ args):
            raise ValueError
        ____ a..(isi..(n, int) ___ n __ args):
            r.. func(*args)
    r.. wrapper
""" 
@int_args
def sum_numbers(*numbers):
    return sum(numbers)

print(sum_numbers(1, 'string', 3)) """