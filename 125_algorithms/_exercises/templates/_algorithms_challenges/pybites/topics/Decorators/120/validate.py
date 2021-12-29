from functools import wraps


___ int_args(func):
    @wraps(func)
    # complete this decorator
    ___ wrapper(*args):
        __ sum(isinstance(n, str) for n in args):
            raise TypeError
        elif sum(isinstance(n, float) for n in args):
            raise TypeError
        elif sum(n < 0 for n in args):
            raise ValueError
        elif all(isinstance(n, int) for n in args):
            return func(*args)
    return wrapper
""" 
@int_args
def sum_numbers(*numbers):
    return sum(numbers)

print(sum_numbers(1, 'string', 3)) """