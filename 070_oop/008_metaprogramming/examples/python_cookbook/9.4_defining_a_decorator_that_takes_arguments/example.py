from functools import wraps
import logging

def logged(level, name=None, message=None):
    '''
    Add logging to a function.  level is the logging
    level, name is the logger name, and message is the
    log message.  If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    print(add(2,3))
    spam()

# Problem
# You want to write a decorator function that takes arguments.
# Solution
# Let’s illustrate the process of accepting arguments with an example. Suppose you want
# to write a decorator that adds logging to a function, but allows the user to specify the
# logging level and other details as arguments. Here is how you might define the decorator:

# On first glance, the implementation looks tricky, but the idea is relatively simple. The
# outermost function logged() accepts the desired arguments and simply makes them
# available to the inner functions of the decorator. The inner function decorate() accepts
# a function and puts a wrapper around it as normal. The key part is that the wrapper is
# allowed to use the arguments passed to logged().
# Discussion
# Writing a decorator that takes arguments is tricky because of the underlying calling
# sequence involved. Specifically, if you have code like this:

# The decoration process evaluates as follows:
# def func(a, b):
# pass
# func = decorator(x, y, z)(func)
# Carefully observe that the result of decorator(x, y, z) must be a callable which, in
# turn, takes a function as input and wraps it. See Recipe 9.7 for another example of a
# decorator taking arguments.