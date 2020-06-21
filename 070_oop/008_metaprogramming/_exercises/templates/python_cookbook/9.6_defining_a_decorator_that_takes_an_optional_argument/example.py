____ functools ____ wraps, partial
____ logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper

# Example use
@logged
def add(x, y):
    return x + y

@logged()
def sub(x, y):
    return x - y

@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')

if __name__ == '__main__':
    ____ logging
    logging.basicConfig(level=logging.DEBUG)
    add(2,3)
    sub(2,3)
    spam()

# Problem
# You would like to write a single decorator that can be used without arguments, such as
# @decorator, or with optional arguments, such as @decorator(x,y,z). However, there
# seems to be no straightforward way to do it due to differences in calling conventions
# between simple decorators and decorators taking arguments.
# Solution
# Here is a variant of the logging code shown in Recipe 9.5 that defines such a decorator:

# As you can see ____ the example, the decorator can be used in both a simple form (i.e.,
# @logged) or with optional arguments supplied (i.e., @logged(level=logging.CRITI
# CAL, name='example')).
# Discussion
# The problem addressed by this recipe is really one of programming consistency. When
# using decorators, most programmers are used to applying them without any arguments
# at all or with arguments, as shown in the example. Technically speaking, a decorator
# where all arguments are optional could be applied, like this:
# @logged()
# def add(x, y):
# return x+y
# However, this is not a form that’s especially common, and might lead to common usage
# errors if programmers forget to add the extra parentheses. The recipe simply makes the
# decorator work with or without parentheses in a consistent way.
# To understand how the code works, you need to have a firm understanding of how
# decorators get applied to functions and their calling conventions. For a simple decorator
# such as this:
# # Example use
# @logged
# def add(x, y):
# return x + y
# The calling sequence is as follows:
# def add(x, y):
# return x + y
# add = logged(add)

# In this case, the function to be wrapped is simply passed to logged as the first argument.
# Thus, in the solution, the first argument of logged() is the function being wrapped. All
# of the other arguments must have default values.
# For a decorator taking arguments such as this:
# @logged(level=logging.CRITICAL, name='example')
# def spam():
# print('Spam!')
# The calling sequence is as follows:
# def spam():
# print('Spam!')
# spam = logged(level=logging.CRITICAL, name='example')(spam)
# On the initial invocation of logged(), the function to be wrapped is not passed. Thus,
# in the decorator, it has to be optional. This, in turn, forces the other arguments to be
# specified by keyword. Furthermore, when arguments are passed, a decorator is supposed
# to return a function that accepts the function and wraps it (see Recipe 9.5). To do this,
# the solution uses a clever trick involving functools.partial. Specifically, it simply
# returns a partially applied version of itself where all arguments are fixed except for the
# function to be wrapped. See Recipe 7.8 for more details about using partial().
