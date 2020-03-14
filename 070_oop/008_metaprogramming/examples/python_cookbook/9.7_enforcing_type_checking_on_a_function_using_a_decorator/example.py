from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Examples

@typeassert(int, int)
def add(x, y):
    return x + y

@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

if __name__ == '__main__':
    print(add(2,3))
    try:
        add(2, 'hello')
    except TypeError as e:
        print(e)

    spam(1, 2, 3)
    spam(1, 'hello', 3)
    try:
        spam(1, 'hello', 'world')
    except TypeError as e:
        print(e)

# Problem
# You want to optionally enforce type checking of function arguments as a kind of assertion
# or contract.
# Solution
# Before showing the solution code, the aim of this recipe is to have a means of enforcing
# type contracts on the input arguments to a function. Here is a short example that illustrates
# the idea:

# Discussion
# This recipe is an advanced decorator example that introduces a number of important
# and useful concepts.
# First, one aspect of decorators is that they only get applied once, at the time of function
# definition. In certain cases, you may want to disable the functionality added by a decorator.
# To do this, simply have your decorator function return the function unwrapped.
# In the solution, the following code fragment returns the function unmodified if the
# value of the global __debug__ variable is set to False (as is the case when Python executes
# in optimized mode with the -O or -OO options to the interpreter):
# ...
# def decorate(func):
# # If in optimized mode, disable type checking
# if not __debug__:
# return func
# ...
# Next, a tricky part of writing this decorator is that it involves examining and working
# with the argument signature of the function being wrapped. Your tool of choice here
# should be the inspect.signature() function. Simply stated, it allows you to extract
# signature information from a callable. For example:

# In the first part of our decorator, we use the bind_partial() method of signatures to
# perform a partial binding of the supplied types to argument names. Here is an example
# of what happens:

# In this partial binding, you will notice that missing arguments are simply ignored (i.e.,
# there is no binding for argument y). However, the most important part of the binding
# is the creation of the ordered dictionary bound_types.arguments. This dictionary maps
# the argument names to the supplied values in the same order as the function signature.
# In the case of our decorator, this mapping contains the type assertions that we’re going
# to enforce.
# In the actual wrapper function made by the decorator, the sig.bind() method is used.
# bind() is like bind_partial() except that it does not allow for missing arguments. So,
# here is what happens:

# Using this mapping, it is relatively easy to enforce the required assertions.

# A somewhat subtle aspect of the solution is that the assertions do not get applied to
# unsupplied arguments with default values. For example, this code works, even though
# the default value of items is of the “wrong” type:

# A final point of design discussion might be the use of decorator arguments versus function
# annotations. For example, why not write the decorator to look at annotations like
# this?

# One possible reason for not using annotations is that each argument to a function can
# only have a single annotation assigned. Thus, if the annotations are used for type assertions,
# they can’t really be used for anything else. Likewise, the @typeassert decorator
# won’t work with functions that use annotations for a different purpose. By using decorator
# arguments, as shown in the solution, the decorator becomes a lot more general
# purpose and can be used with any function whatsoever—even functions that use
# annotations.
# More information about function signature objects can be found in PEP 362, as well as
# the documentation for the inspect module. Recipe 9.16 also has an additional example.

