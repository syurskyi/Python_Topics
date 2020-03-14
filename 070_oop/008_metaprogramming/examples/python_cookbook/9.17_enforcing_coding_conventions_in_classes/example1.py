# A metaclass that disallows mixed case identifier names

class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)

class Root(metaclass=NoMixedCaseMeta):
    pass

class A(Root):
    def foo_bar(self):      # Ok
        pass

print('**** About to generate a TypeError')
class B(Root):
    def fooBar(self):       # TypeError
        pass


# Problem
# Your program consists of a large class hierarchy and you would like to enforce certain
# kinds of coding conventions (or perform diagnostics) to help maintain programmer
# sanity.
# Solution
# If you want to monitor the definition of classes, you can often do it by defining a
# metaclass. A basic metaclass is usually defined by inheriting from type and redefining
# its __new__() method or __init__() method. For example:

# To use a metaclass, you would generally incorporate it into a top-level base class from
# which other objects inherit. For example:

# A key feature of a metaclass is that it allows you to examine the contents of a class at the
# time of definition. Inside the redefined __init__() method, you are free to inspect the
# class dictionary, base classes, and more. Moreover, once a metaclass has been specified
# for a class, it gets inherited by all of the subclasses. Thus, a sneaky framework builder
# can specify a metaclass for one of the top-level classes in a large hierarchy and capture
# the definition of all classes under it.
# As a concrete albeit whimsical example, here is a metaclass that rejects any class definition
# containing methods with mixed-case names (perhaps as a means for annoying
# Java programmers):

# As a more advanced and useful example, here is a metaclass that checks the definition
# of redefined methods to make sure they have the same calling signature as the original
# method in the superclass.

# Such warnings might be useful in catching subtle program bugs. For example, code that
# relies on keyword argument passing to a method will break if a subclass changes the
# argument names.
# Discussion
# In large object-oriented programs, it can sometimes be useful to put class definitions
# under the control of a metaclass. The metaclass can observe class definitions and be
# used to alert programmers to potential problems that might go unnoticed (e.g., using
# slightly incompatible method signatures).

# One might argue that such errors would be better caught by program analysis tools or
# IDEs. To be sure, such tools are useful. However, if you’re creating a framework or library
# that’s going to be used by others, you often don’t have any control over the rigor of their
# development practices. Thus, for certain kinds of applications, it might make sense to
# put a bit of extra checking in a metaclass if such checking would result in a better user
# experience.
# The choice of redefining __new__() or __init__() in a metaclass depends on how you
# want to work with the resulting class. __new__() is invoked prior to class creation and
# is typically used when a metaclass wants to alter the class definition in some way (by
# changing the contents of the class dictionary). The __init__() method is invoked after
# a class has been created, and is useful if you want to write code that works with the fully
# formed class object. In the last example, this is essential since it is using the super()
# function to search for prior definitions. This only works once the class instance has been
# created and the underlying method resolution order has been set.
# The last example also illustrates the use of Python’s function signature objects. Essentially,
# the metaclass takes each callable definition in a class, searches for a prior definition
# (if any), and then simply compares their calling signatures using inspect.signature().
# Last, but not least, the line of code that uses super(self, self) is not a typo. When
# working with a metaclass, it’s important to realize that the self is actually a class object.
# So, that statement is actually being used to find definitions located further up the class
# hierarchy that make up the parents of self.