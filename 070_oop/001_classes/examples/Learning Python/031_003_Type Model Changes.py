
class C:
    pass                       # Classic classes in 2.6

I = C()

print('#' * 23 + ' Instances are made from classes')
print(type(I))                             # Instances are made from classes
# <type 'instance'>
print(I.__class__)
# <class __main__.C at 0x025085A0>

print('#' * 23 + ' But classes are not the same as types')
print(type(C))                             # But classes are not the same as types
# <type 'classobj'>
print(C.__class__)
# AttributeError: class C has no attribute '__class__'

print(type([1, 2, 3]))

print(type(list))

print(list.__class__)


class C(object):
    pass               # New-style classes in 2.6

I = C()
print('#' * 23 + ' Type of instance is class its made from')
print(type(I))                             # Type of instance is class it's made from
print(I.__class__)

print('#' * 23 + ' Classes are user-defined types')
print(type(C))                             # Classes are user-defined types
print(C.__class__)

print('#' * 23 + ' Built-in types work the same way')
print(type([1, 2, 3]))                     # Built-in types work the same way
print(type(list))
print(list.__class__)


class C:
    pass                       # All classes are new-style in 3.0

I = C()
print('#' * 23 + ' Type of instance is class its made from')
print(type(I))                             # Type of instance is class it's made from
print(I.__class__)

print('#' * 23 + ' Class is a type, and type is a class')
print(type(C))                             # Class is a type, and type is a class
print(C.__class__)

print('#' * 23 + ' Classes and built-in types work the same')
print(type([1, 2, 3]))                     # Classes and built-in types work the same
print(type(list))
print(list.__class__)
