# Example of making a class manually from parts

# Methods
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

cls_dict = {
    '__init__' : __init__,
    'cost' : cost,
}

# Make a class
import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))

if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)
    print(s)
    print(s.cost())

# Problem
# You’re writing code that ultimately needs to create a new class object. You’ve thought
# about emitting emit class source code to a string and using a function such as exec()
# to evaluate it, but you’d prefer a more elegant solution.
# Solution
# You can use the function types.new_class() to instantiate new class objects. All you
# need to do is provide the name of the class, tuple of parent classes, keyword arguments,
# and a callback that populates the class dictionary with members. For example:

# A subtle facet of the solution is the assignment to Stock.__module__ after the call to
# types.new_class(). Whenever a class is defined, its __module__ attribute contains the
# name of the module in which it was defined. This name is used to produce the output
# made by methods such as __repr__(). It’s also used by various libraries, such as pick
# le. Thus, in order for the class you make to be “proper,” you need to make sure this
# attribute is set accordingly.
# If the class you want to create involves a different metaclass, it would be specified in the
# third argument to types.new_class(). For example:

# The third argument may also contain other keyword arguments. For example, a class
# definition like this

# The fourth argument to new_class() is the most mysterious, but it is a function that
# receives the mapping object being used for the class namespace as input. This is normally
# a dictionary, but it’s actually whatever object gets returned by the __prepare__() method,
# as described in Recipe 9.14. This function should add new entries to the namespace
# using the update() method (as shown) or other mapping operations.
# Discussion
# Being able to manufacture new class objects can be useful in certain contexts. One of
# the more familiar examples involves the collections.namedtuple() function. For
# example:

# namedtuple() uses exec() instead of the technique shown here. However, here is a
# simple variant that creates a class directly:

# The last part of this code uses a so-called “frame hack” involving sys._getframe() to
# obtain the module name of the caller. Another example of frame hacking appears in
# Recipe 2.15.

# One important aspect of the technique used in this recipe is its proper support for
# metaclasses. You might be inclined to create a class directly by instantiating a metaclass
# directly. For example:
# Stock = type('Stock', (), cls_dict)
# The problem is that this approach skips certain critical steps, such as invocation of the
# metaclass __prepare__() method. By using types.new_class() instead, you ensure
# that all of the necessary initialization steps get carried out. For instance, the callback
# function that’s given as the fourth argument to types.new_class() receives the mapping
# object that’s returned by the __prepare__() method.
# If you only want to carry out the preparation step, use types.prepare_class(). For
# example:
# import types
# metaclass, kwargs, ns = types.prepare_class('Stock', (), {'metaclass': type})
# This finds the appropriate metaclass and invokes its __prepare__() method. The
# metaclass, remaining keyword arguments, and prepared namespace are then returned.
# For more information, see PEP 3115, as well as the Python documentation.

