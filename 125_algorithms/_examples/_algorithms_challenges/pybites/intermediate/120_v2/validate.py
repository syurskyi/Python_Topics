from functools import wraps


def int_args(func):
    @wraps(func)
    # complete this decorator


    def wrapper(*args):

        for arg in args:
            if type(arg) != int:
                raise TypeError("All arguments passed in must be integers")
            

            if arg <0:
                raise ValueError("All arguments must be non-negative integers")


        return func(*args)


    return wrapper





