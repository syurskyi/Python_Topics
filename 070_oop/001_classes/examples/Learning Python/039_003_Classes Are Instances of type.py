print(type([]))                   # In 3.0 list is instance of list type
# <class 'list'>
print(type(type([])))               # Type of list is type class
# <class 'type'>

print(type(list))                   # Same, but with type names
# <class 'type'>
print(type(type))                   # Type of type is type: top of hierarchy
# <class 'type'>

print(type([]))                    # In 2.6, type is a bit different
# <type 'list'>
print(type(type([])))
# <type 'type'>

print(type(list))
# <type 'type'>
print(type(type))
# <type 'type'>

class C: pass                 # 3.0 class object (new-style)

X = C()                       # Class instance object

print(type(X))                       # Instance is instance of class
# <class '__main__.C'>
print(X.__class__)                  # Instance's class
# <class '__main__.C'>

print(type(C))                      # Class is instance of type
# <class 'type'>
print(C.__class__)                  # Class's class is type
# <class 'type'>


class C(object): pass         # In 2.6 new-style classes,
                              # classes have a class too
X = C()

print(type(X))
# <class '__main__.C'>
print(type(C))
# <type 'type'>

print(X.__class__)
# <class '__main__.C'>
print(C.__class__)
# <type 'type'>

class C: pass                 # In 2.6 classic classes,
                             # classes have no class themselves
X = C()

print(type(X))
# <type 'instance'>
print(type(C))
# <type 'classobj'>

print(X.__class__)
# <class __main__.C at 0x005F85A0>
print(C.__class__)
# AttributeError: class C has no attribute '__class__'

