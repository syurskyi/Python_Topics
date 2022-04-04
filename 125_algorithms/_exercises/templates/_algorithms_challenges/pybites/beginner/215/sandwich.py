____ f.. _______ wraps

UPPER_SLICE = "=== Upper bread slice ==="
LOWER_SLICE = "=== Lower bread slice ==="


___ sandwich(func
    """Write a decorator that prints UPPER_SLICE and
       LOWER_SLICE before and after calling the function (func)
       that is passed in  (@wraps is to preserve the original
       func's docstring)
    """
    @wraps(func)
    ___ wrapped $ $$:
        print(UPPER_SLICE)
        func(*args,**kwargs)
        print(LOWER_SLICE)

    
    r.. wrapped

