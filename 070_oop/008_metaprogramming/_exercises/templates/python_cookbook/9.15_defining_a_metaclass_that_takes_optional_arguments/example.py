# Example of a metaclass that takes optional arguments

class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing
        return super().__prepare__(name, bases)

    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        return super().__new__(cls, name, bases, ns)
        
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        super().__init__(name, bases, ns)

# Examples
class A(metaclass=MyMeta, debug=True, synchronize=True):
    pass

class B(metaclass=MyMeta):
    pass

class C(metaclass=MyMeta, synchronize=True):
    pass

    
# Problem
# You want to define a metaclass that allows class definitions to supply optional arguments,
# possibly to control or configure aspects of processing during type creation.
# Solution
# When defining classes, Python allows a metaclass to be specified using the metaclass
# keyword argument in the class statement. For example, with abstract base classes:

# However, in custom metaclasses, additional keyword arguments can be supplied, like
# this:

# To support such keyword arguments in a metaclass, make sure you define them on the
# __prepare__(), __new__(), and __init__() methods using keyword-only arguments,
# like this:

# Discussion
# Adding optional keyword arguments to a metaclass requires that you understand all of
# the steps involved in class creation, because the extra arguments are passed to every
# method involved. The __prepare__() method is called first and used to create the class
# namespace prior to the body of any class definition being processed. Normally, this
# method simply returns a dictionary or other mapping object. The __new__() method
# is used to instantiate the resulting type object. It is called after the class body has been
# fully executed. The __init__() method is called last and used to perform any additional
# initialization steps.
# When writing metaclasses, it is somewhat common to only define a __new__() or
# __init__() method, but not both. However, if extra keyword arguments are going to
# be accepted, then both methods must be provided and given compatible signatures. The
# default __prepare__() method accepts any set of keyword arguments, but ignores them.
# You only need to define it yourself if the extra arguments would somehow affect management
# of the class namespace creation.
# The use of keyword-only arguments in this recipe reflects the fact that such arguments
# will only be supplied by keyword during class creation.
# The specification of keyword arguments to configure a metaclass might be viewed as
# an alternative to using class variables for a similar purpose. For example:

# The advantage to supplying such parameters as an argument is that they don’t pollute
# the class namespace with extra names that only pertain to class creation and not the
# subsequent execution of statements in the class. In addition, they are available to the
# __prepare__() method, which runs prior to processing any statements in the class body.
# Class variables, on the other hand, would only be accessible in the __new__() and
# __init__() methods of a metaclass.
