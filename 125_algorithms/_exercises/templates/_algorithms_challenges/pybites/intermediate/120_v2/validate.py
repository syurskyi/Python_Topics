____ functools _______ wraps


___ int_args(func):
    @wraps(func)
    # complete this decorator


    ___ wrapper(*args):

        ___ arg __ args:
            __ type(arg) != int:
                raise TypeError("All arguments passed in must be integers")
            

            __ arg <0:
                raise ValueError("All arguments must be non-negative integers")


        r.. func(*args)


    r.. wrapper





