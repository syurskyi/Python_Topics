from functools import wraps


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))

    return inner


@counter
def add(a: int, b: int = 10) -> int:
    """
    returns sum of two integers
    """
    return a + b


inspect.getsource(add)
inspect.signature(add)
inspect.signature(add).parameters