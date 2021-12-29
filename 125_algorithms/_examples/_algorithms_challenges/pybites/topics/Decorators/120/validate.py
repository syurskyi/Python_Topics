from functools import wraps


def int_args(func):
    @wraps(func)
    # complete this decorator
    def wrapper(*args):
        if sum(isinstance(n, str) for n in args):
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