# Python added the enum module to the standard library in version 3.4. The Python documentation describes an enum like
# this: An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration,
# the members can be compared by identity, and the enumeration itself can be iterated over.
#
# Let's look at how you might create an Enum object:
#
from enum import Enum

class AnimalEnum(Enum):
    HORSE = 1
    COW = 2
    CHICKEN = 3
    DOG = 4

print(AnimalEnum.CHICKEN)
# AnimalEnum.CHICKEN
print(repr(AnimalEnum.CHICKEN))
# <AnimalEnum.CHICKEN: 3>
# Here we create an Enumeration class called AnimalEnum. Inside the class, we create class attributes called enumeration
# members, which are constants. When you try to print out an enum member, you will just get back the same string.
# But if you print out the repr of the enum member, you will get the enum member and its value.
# If you try to modify an enum member, Python will raise an AttributeError:
#
# >>> AnimalEnum.CHICKEN = 5
# Traceback (most recent call last):
#   Python Shell, prompt 5, line 1
#   File "C:\Users\mike\AppData\Local\Programs\PYTHON\PYTHON36-32\Lib\enum.py", line 361, in __setattr__
#     raise AttributeError('Cannot reassign members.')
# builtins.AttributeError: Cannot reassign members.

# Enum members have some properties you can use to get their name and value:
#
AnimalEnum.CHICKEN.name
# 'CHICKEN'
AnimalEnum.CHICKEN.value
# 3
# Enumerations also support iteration. So you can do something fun like this:
#
for animal in AnimalEnum:
    print('Name: {}  Value: {}'.format(animal, animal.value))
# Name: AnimalEnum.HORSE  Value: 1
# Name: AnimalEnum.COW  Value: 2
# Name: AnimalEnum.CHICKEN  Value: 3
# Name: AnimalEnum.DOG  Value: 4

# Python's enumerations do not allow you to create enum members with the same name:
#
class Shapes(Enum):
    CIRCLE = 1
    SQUARE = 2
    SQUARE = 3

# Traceback (most recent call last):
#   Python Shell, prompt 13, line 1
#   Python Shell, prompt 13, line 4
#   File "C:\Users\mike\AppData\Local\Programs\PYTHON\PYTHON36-32\Lib\enum.py", line 92, in __setitem__
#     raise TypeError('Attempted to reuse key: %r' % key)
# builtins.TypeError: Attempted to reuse key: 'SQUARE'

# As you can see, when you try to reuse an enum member name, it will raise a TypeError.
# You can also create an Enum like this:
#
AnimalEnum = Enum('Animal', 'HORSE COW CHICKEN DOG')
print(AnimalEnum)
# <enum 'Animal'>
AnimalEnum.CHICKEN
# <Animal.CHICKEN: 3>
# Personally, I think that is really neat!
#
# Enum Member Access
# Interestingly enough, there are multiple ways to access enum members. For example, if you don't know which enum
# is which, you can just call the enum directly and pass it a value:
#
AnimalEnum(2)
# <AnimalEnum.COW: 2>
#
# If you happen to pass in an invalid value, then Python raises a ValueError
#
# >>> AnimalEnum(8)
# Traceback (most recent call last):
#   Python Shell, prompt 11, line 1
#   File "C:\Users\mike\AppData\Local\Programs\PYTHON\PYTHON36-32\Lib\enum.py", line 291, in __call__
#     return cls.__new__(cls, value)
#   File "C:\Users\mike\AppData\Local\Programs\PYTHON\PYTHON36-32\Lib\enum.py", line 533, in __new__
#     return cls._missing_(value)
#   File "C:\Users\mike\AppData\Local\Programs\PYTHON\PYTHON36-32\Lib\enum.py", line 546, in _missing_
#     raise ValueError("%r is not a valid %s" % (value, cls.__name__))
# builtins.ValueError: 8 is not a valid AnimalEnum

# You may also access an enumeration by name:
#
AnimalEnum['CHICKEN']
# <AnimalEnum.CHICKEN: 3>

# Enum Niceties
# The enum module also has a couple of other fun things you can import. For example, you can create automatic values
# for your enumerations:
#
from enum import auto, Enum

class Shapes(Enum):
    CIRCLE = auto()
    SQUARE = auto()
    OVAL = auto()
Shapes.CIRCLE
# <Shapes.CIRCLE: 1>

# You can also import a handy enum decorator to make sure that your enumeration members are unique:
#
@unique
class Shapes(Enum):
    CIRCLE = 1
    SQUARE = 2
    TRIANGLE = 1

# Traceback (most recent call last):
#   Python Shell, prompt 18, line 2
#   File "C:\Users\mike\AppData\Local\Programs\PYTHON\PYTHON36-32\Lib\enum.py", line 830, in unique
#     (enumeration, alias_details))
# builtins.ValueError: duplicate values found in <enum 'Shapes'>: TRIANGLE -> CIRCLE
# Here we create an enumeration that has two members trying to map to the same value. Because we added the @unique
# decorator, a ValueError is raised if there are any duplicate values in the enum members. If you do not have
# the @unique decorator applied, then you can have enum members with the same value.
#
# Wrapping Up
# While I don't think the enum module is really necessary for Python, it is a neat tool to have available.
# The documentation has a lot more examples and demonstrates other types of enums, so it is definitely worth a read.
