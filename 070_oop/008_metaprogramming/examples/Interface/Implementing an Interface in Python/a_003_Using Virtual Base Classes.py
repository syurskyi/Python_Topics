# Using Virtual Base Classes
# In the previous example, issubclass(EmlParserNew, UpdatedInformalParserInterface) returned True, even though
# UpdatedInformalParserInterface did not appear in the EmlParserNew MRO. That's because UpdatedInformalParserInterface
# is a virtual base class of EmlParserNew.
#
# The key difference between these and standard subclasses is that virtual base classes use the .__subclasscheck__()
# dunder method to implicitly check if a class is a virtual subclass of the superclass. Additionally, virtual base
# classes don't appear in the subclass MRO.

class PersonMeta(type):
    """A person metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and
                callable(subclass.name) and
                hasattr(subclass, 'age') and
                callable(subclass.age))

class PersonSuper:
    """A person superclass"""
    def name(self) -> str:
        pass

    def age(self) -> int:
        pass

class Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass."""
    pass


# Here, you have the setup for creating your virtual base classes:
#
# The metaclass PersonMeta
# The base class PersonSuper
# The Python interface Person
# Now that the setup for creating virtual base classes is done you'll define two concrete classes, Employee and Friend.
# The Employee class inherits from PersonSuper, while Friend implicitly inherits from Person:

# Inheriting subclasses

class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__
    """
    pass

class Friend:
    """Built implicitly from Person
    Friend is a virtual subclass of Person since
    both required methods exist.
    Person not in Friend.__mro__
    """
    def name(self):
        pass

    def age(self):
        pass

# Although Friend does not explicitly inherit from Person, it implements .name() and .age(), so Person becomes
# a virtual base class of Friend. When you run issubclass(Friend, Person) it should return True, meaning that Friend
# is a subclass of Person.
# The following UML diagram shows what happens when you call issubclass() on the Friend class:
#
# virtual base class
#
# Taking a look at PersonMeta, you'll notice that there's another dunder method called .__instancecheck__().
# This method is used to check if instances of Friend are created from the Person interface.
# Your code will call .__instancecheck__() when you use isinstance(Friend, Person).
