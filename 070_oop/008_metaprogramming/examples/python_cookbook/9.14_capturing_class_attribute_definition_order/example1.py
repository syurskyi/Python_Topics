# Example of capturing class definition order

from collections import OrderedDict

# A set of descriptors for various types
class Typed:
    _expected_type = type(None)
    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Expected ' +str(self._expected_type))
        instance.__dict__[self._name] = value

class Integer(Typed):
    _expected_type = int

class Float(Typed):
    _expected_type = float

class String(Typed):
    _expected_type = str

# Metaclass that uses an OrderedDict for class body
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()

# Example class that uses the definition order to initialize members
class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self,name)) for name in self._order)

# Example use
class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

if __name__ == '__main__':
    s = Stock('GOOG',100,490.1)
    print(s.name)
    print(s.as_csv())
    try:
        t = Stock('AAPL','a lot', 610.23)
    except TypeError as e:
        print(e)

# Problem
# You want to automatically record the order in which attributes and methods are defined
# inside a class body so that you can use it in various operations (e.g., serializing, mapping
# to databases, etc.).
# Solution
# Capturing information about the body of class definition is easily accomplished through
# the use of a metaclass. Here is an example of a metaclass that uses an OrderedDict to
# capture definition order of descriptors:

# In this metaclass, the definition order of descriptors is captured by using an Ordered
# Dict during the execution of the class body. The resulting order of names is then extracted
# from the dictionary and stored into a class attribute _order. This can then be
# used by methods of the class in various ways. For example, here is a simple class that
# uses the ordering to implement a method for serializing the instance data as a line of
# CSV data:

# Discussion
# The entire key to this recipe is the __prepare__() method, which is defined in the
# OrderedMeta metaclass. This method is invoked immediately at the start of a class definition
# with the class name and base classes. It must then return a mapping object to
# use when processing the class body. By returning an OrderedDict instead of a normal
# dictionary, the resulting definition order is easily captured.
# It is possible to extend this functionality even further if you are willing to make your
# own dictionary-like objects. For example, consider this variant of the solution that rejects
# duplicate definitions:

# A final important part of this recipe concerns the treatment of the modified dictionary
# in the metaclass __new__() method. Even though the class was defined using an alter‐

# native dictionary, you still have to convert this dictionary to a proper dict instance
# when making the final class object. This is the purpose of the d = dict(clsdict)
# statement.
# Being able to capture definition order is a subtle but important feature for certain kinds
# of applications. For instance, in an object relational mapper, classes might be written in
# a manner similar to that shown in the example:
# class Stock(Model):
# name = String()
# shares = Integer()
# price = Float()
# Underneath the covers, the code might want to capture the definition order to map
# objects to tuples or rows in a database table (e.g., similar to the functionality of the
# as_csv() method in the example). The solution shown is very straightforward and often
# simpler than alternative approaches (which typically involve maintaining hidden counters
# within the descriptor classes).
