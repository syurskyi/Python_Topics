# Example of defining a decorator as a class
import types
from functools import wraps
       
class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

# Example

@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

if __name__ == '__main__':
    print(add(2,3))
    print(add(4,5))
    print('ncalls:', add.ncalls)

    s = Spam()
    s.bar(1)
    s.bar(2)
    s.bar(3)
    print('ncalls:', Spam.bar.ncalls)

# Problem
# You want to wrap functions with a decorator, but the result is going to be a callable
# instance. You need your decorator to work both inside and outside class definitions.
# Solution
# To define a decorator as an instance, you need to make sure it implements the
# __call__() and __get__() methods. For example, this code defines a class that puts a
# simple profiling layer around another function:

# Discussion
# Defining a decorator as a class is usually straightforward. However, there are some rather
# subtle details that deserve more explanation, especially if you plan to apply the decorator
# to instance methods.
# First, the use of the functools.wraps() function serves the same purpose here as it
# does in normal decorators—namely to copy important metadata from the wrapped
# function to the callable instance.
# Second, it is common to overlook the __get__() method shown in the solution. If you
# omit the __get__() and keep all of the other code the same, you’ll find that bizarre
# things happen when you try to invoke decorated instance methods. For example

# The reason it breaks is that whenever functions implementing methods are looked up
# in a class, their __get__() method is invoked as part of the descriptor protocol, which

# is described in Recipe 8.9. In this case, the purpose of __get__() is to create a bound
# method object (which ultimately supplies the self argument to the method). Here is
# an example that illustrates the underlying mechanics:

# In this recipe, the __get__() method is there to make sure bound method objects get
# created properly. type.MethodType() creates a bound method manually for use here.
# Bound methods only get created if an instance is being used. If the method is accessed
# on a class, the instance argument to __get__() is set to None and the Profiled instance
# itself is just returned. This makes it possible for someone to extract its ncalls attribute,
# as shown.
# If you want to avoid some of this of this mess, you might consider an alternative formulation
# of the decorator using closures and nonlocal variables, as described in
# Recipe 9.5. For example:

# This example almost works in exactly the same way except that access to ncalls is now
# provided through a function attached as a function attribute. For example: