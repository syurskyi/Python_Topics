# Example of code that enforces signatures on an __init__ function

from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)

class Structure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

# Example use
class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')

class Point(Structure):
    __signature__ = make_sig('x', 'y')

# Example instantiation tests
if __name__ == '__main__':
    s1 = Stock('ACME', 100, 490.1)
    print(s1.name, s1.shares, s1.price)

    s2 = Stock(shares=100, name='ACME', price=490.1)
    print(s2.name, s2.shares, s2.price)

    # Not enough args
    try:
        s3 = Stock('ACME', 100)
    except TypeError as e:
        print(e)

    # Too many args
    try:
        s4 = Stock('ACME', 100, 490.1, '12/21/2012')
    except TypeError as e:
        print(e)

    # Replicated args
    try:
        s5 = Stock('ACME', 100, name='ACME', price=490.1)
    except TypeError as e:
        print(e)

# Problem
# You’ve written a function or method that uses *args and **kwargs, so that it can be
# general purpose, but you would also like to check the passed arguments to see if they
# match a specific function calling signature.
# Solution
# For any problem where you want to manipulate function calling signatures, you should
# use the signature features found in the inspect module. Two classes, Signature and
# Parameter, are of particular interest here. Here is an interactive example of creating a
# function signature:

# Once you have a signature object, you can easily bind it to *args and **kwargs using
# the signature’s bind() method, as shown in this simple example:

# As you can see, the binding of a signature to the passed arguments enforces all of the
# usual function calling rules concerning required arguments, defaults, duplicates, and
# so forth.
# Here is a more concrete example of enforcing function signatures. In this code, a base
# class has defined an extremely general-purpose version of __init__(), but subclasses
# are expected to supply an expected signature.

# Discussion
# The use of functions involving *args and **kwargs is very common when trying to
# make general-purpose libraries, write decorators or implement proxies. However, one
# downside of such functions is that if you want to implement your own argument checking,
# it can quickly become an unwieldy mess. As an example, see Recipe 8.11. The use
# of a signature object simplifies this.
# In the last example of the solution, it might make sense to create signature objects
# through the use of a custom metaclass. Here is an alternative implementation that shows
# how to do this:

# When defining custom signatures, it is often useful to store the signature in a special
# attribute __signature__, as shown. If you do this, code that uses the inspect module
# to perform introspection will see the signature and report it as the calling convention.
# For example:
    

    
