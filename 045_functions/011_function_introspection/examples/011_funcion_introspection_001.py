# Annotations


def my_func(a: 'annotation for a',
            b: 'annotation for b') -> 'annotation for return':
    return a * b


help(my_func)


# The annotations can be any expression, not just strings:

x = 3
y = 5


def my_func(a: str) -> 'a repeated ' + str(max(3, 5)) + ' times':
    return a*max(x, y)

help(my_func)

# Just like docstrings are stored in the __doc__ property, annotations are stored in the __annotations__ property
# - a dictionary whose keys are the parameter names, and values are the annotation.

x = 3
y = 5
def my_func(a: str) -> 'a repeated ' + str(max(3, 5)) + ' times':
	return a*max(x, y)

my_func.__annotations__

# Annotations will work with default parameters too: just specify the default after the annotation


def my_func(a: str = 'a', b: int = 1)->str:
    return a*b


help(my_func)
my_func()
my_func('abc', 3)


def my_func(a: int = 0, *args: 'additional args'):
    print(a, args)


my_func.__annotations__

help(my_func)

# Function Introspection
# The name attribute holds the function's name:
def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass

f = my_func


my_func.__name__
f.__name__

# Function Introspection
# The defaults attribute is a tuple containing any positional parameter defaults:

def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass
f = my_func

my_func.__defaults__
my_func.__kwdefaults__


# Function Introspection
# The code attribute contains a code object:

def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

my_func('a', 100)

my_func.__code__

dir(my_func.__code__)

# Function Introspection
#
# Attribute co_varnames is a tuple containing the parameter names and local variables:

def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass

f = my_func

my_func.__code__.co_varnames


# Function Introspection
# Attribute co_argcount returns the number of arguments (minus any * and ** args)

def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass

f = my_func
my_func.__code__.co_argcount

# The inspect module

def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

my_func('a', 100)

import inspect
inspect.isfunction(my_func)
inspect.ismethod(my_func)

# Introspecting Callable Code

# def fact(n: "some non-negative integer") -> "n! or 0 if n < 0": """Calculates the factorial of a non-negative integer n
#
# If n is negative, returns 0.
# """
#     if n < 0:
#         return 0
#     elif n <= 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
# inspect.getsource(fact)
