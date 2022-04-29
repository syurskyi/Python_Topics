import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result
    return wrapper


# Example 2
@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


# Example 3
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))

fibonacci = trace(fibonacci)


# Example 4
fibonacci(3)


# Example 5
print(fibonacci)


# Example 6
try:
    # Example of how pickle breaks
    import pickle
    
    def my_func():
        return 1
    
    # This will be okay
    print(pickle.dumps(my_func))
    
    @trace
    def my_func2():
        return 2
    
    # This will explode
    print(pickle.dumps(my_func2))
except:
    logging.exception('Expected')
else:
    assert False


# Example 7
help(fibonacci)


# Example 8
from functools import wraps
def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result
    return wrapper

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) +
            fibonacci(n - 1))


# Example 9
help(fibonacci)
