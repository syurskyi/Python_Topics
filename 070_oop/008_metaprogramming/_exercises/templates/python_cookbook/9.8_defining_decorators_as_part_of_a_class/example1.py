from functools import wraps

class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper

# Example
# As an instance method
a = A()

@a.decorator1
def spam():
    pass

# As a class method
@A.decorator2
def grok():
    pass

spam()
grok()


# Problem
# You want to define a decorator inside a class definition and apply it to other functions
# or methods.
# Solution
# Defining a decorator inside a class is straightforward, but you first need to sort out the
# manner in which the decorator will be applied. Specifically, whether it is applied as an
# instance or a class method. Here is an example that illustrates the difference:

# Here is an example of how the two decorators would be applied:

# If you look carefully, you’ll notice that one is applied from an instance a and the other
# is applied from the class A.
# Discussion
# Defining decorators in a class might look odd at first glance, but there are examples of
# this in the standard library. In particular, the built-in @property decorator is actually a
# class with getter(), setter(), and deleter() methods that each act as a decorator.
# For example:

# The key reason why it’s defined in this way is that the various decorator methods are
# manipulating state on the associated property instance. So, if you ever had a problem
# where decorators needed to record or combine information behind the scenes, it’s a
# sensible approach.
# A common confusion when writing decorators in classes is getting tripped up by the
# proper use of the extra self or cls arguments in the decorator code itself. Although
# the outermost decorator function, such as decorator1() or decorator2(), needs to
# provide a self or cls argument (since they’re part of a class), the wrapper function
# created inside doesn’t generally need to include an extra argument. This is why the
# wrapper() function created in both decorators doesn’t include a self argument. The
# only time you would ever need this argument is in situations where you actually needed

# to access parts of an instance in the wrapper. Otherwise, you just don’t have to worry
# about it.
# A final subtle facet of having decorators defined in a class concerns their potential use
# with inheritance. For example, suppose you want to apply one of the decorators defined
# in class A to methods defined in a subclass B. To do that, you would need to write code
# like this:
# class B(A):
# @A.decorator2
# def bar(self):
# pass
# In particular, the decorator in question has to be defined as a class method and you have
# to explicitly use the name of the superclass A when applying it. You can’t use a name
# such as @B.decorator2, because at the time of method definition, class B has not yet
# been created.