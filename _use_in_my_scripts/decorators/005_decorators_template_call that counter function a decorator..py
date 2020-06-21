def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner


@counter
def mult(a: float, b: float = 1, c: float = 1) -> float:
    """
    returns the product of a, b, and c
    """
    return a * b * c


mult(1, 2, 3)
mult(2, 2, 2)

# Let's do a little bit of introspection on our two decorated functions:

add.__name__
mult.__name__

