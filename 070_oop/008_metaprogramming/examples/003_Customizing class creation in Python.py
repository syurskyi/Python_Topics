# When one thinks of ways of customizing classes at creation time, people probably typically think of metaclasses
# and class decorators. Metaclasses are at typically viewed as the beginning of class creation while class decorators
# are at the end. But what you may not know is that there are two other steps in class creation that you can tweak:
# __prepare__() and __init_subclass__() (added in Python 3.0 and 3.6, respectively).
#
# The __prepare__() hook is used to specify the object used for the class' namespace during construction
# (the object gets copied into a dict in the end for final storage into __dict__). The method is specified on
# a metaclass and called before __new__(). Historically the __prepare__() method has been used to return OrderedDict
# so that the definition order of things in a class can be known later on. But since the returned object is used
# as the class' namespace you can also use it to inject objects to use in your class' definition.
#
# To take an idea from David Beazley, you can abuse __prepare__() so you can define an ABC so that abstractmethod
# is implicitly available in the class definition.


import abc
from abc import abstractmethod

class DaABC(abc.ABCMeta):
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        return {"abstractmethod": abc.abstractmethod}


# Using this metaclass gives you access to abstractmethod without having to get it from abc.

class Foo(metaclass=DaABC):
    # Notice not `abc.abstractmethod`.
    @abstractmethod
    def meth(self):
        pass

# This works because the way classes are created is essentially by taking the class' body and passing it
# to exec() with the result of calling __prepare__() as the locals.
#
# Another way to tweak class creation is __init_subclass__(). The method gets called when the defining class
# gets subclassed. It's passed both the subclass and any keyword arguments provided to the class definition line.
#
# To help show a way to use this, I realized that you could abuse variable type annotations to make
# a "scary" version of Hynek Schlawack's attrs project. Basically the following class automatically defines
# an __init__() and (optionally) the __repr__() for a class based on variable type annotations.


class ScareHynek:

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        attrs = tuple(cls.__annotations__.keys())
        def __init__(self, *args, **kwargs):
            # Skimping on the argument-checking because I'm lazy.
            if len(args) > len(attrs):
                raise TypeError("too many positional arguments")
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
            for attr, val in kwargs.items():
                if attr not in attrs:
                    raise TypeError("got an unexpected keyword argument {!r}")
                setattr(self, attr, val)
        cls.__init__ = __init__
        if kwargs.get("repr", True):
            repr_format = "<" + ", ".join(f"{attr}={{{attr}!r}}" for attr in attrs) + ">"
            def __repr__(self):
                all_attrs = self.__class__.__dict__.copy()
                all_attrs.update(self.__dict__)
                return repr_format.format_map(all_attrs)
            cls.__repr__ = __repr__

# This then lets you create simple Python objects that you may have created using types.SimpleNamespace instead
# (aside: please don't abuse collections.namedtuple to make a simple Python object; the class is meant to help
# porting APIs that return a tuple to a more object-oriented one, so starting with namedtuple means you end up
# leaking a tuple API that you probably didn't want to begin with).


class Simple(ScareHynek):
    question: str
    answer: int = 42

ins = Simple(question="Ultimate Question of Life, The Universe, and Everything")
print(repr(ins))
# Prints "# <question='Ultimate Question of Life, The Universe, and Everything', answer=42>"


# You can also use keyword arguments to the class definition to skip the __repr__() definition.


class Plain(ScareHynek, repr=False):
    x: int

ins = Plain(42)
print(repr(ins))
# Prints "<class_creation.Plain object at 0x100f91198>"


# As with all things that tweak class creation, you must be very careful to not abuse this stuff.
# Adjusting how classes are created can be very difficult to debug and so should only be used when you have a really
# legitimate use-case. But this stuff is worth knowing about in case you run into code that uses it or you have
# a real need for it when there are no other reasonable options.
