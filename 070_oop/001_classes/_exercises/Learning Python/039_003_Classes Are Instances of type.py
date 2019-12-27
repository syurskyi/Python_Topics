# print(ty..([]))                   # In 3.0 list is instance of list type
# # <class 'list'>
# print(ty..(ty..([])))               # Type of list is type class
# # <class 'type'>
#
# print(ty..(li..                   # Same, but with type names
# # <class 'type'>
# print(ty..(ty..))                   # Type of type is type: top of hierarchy
# # <class 'type'>
#
# print(ty..([]))                    # In 2.6, type is a bit different
# # <type 'list'>
# print(ty..(ty..([])))
# # <type 'type'>
#
# print(ty..(li..
# # <type 'type'>
# print(ty..(ty..))
# # <type 'type'>
#
# class C: pass                 # 3.0 class object (new-style)
#
# X = C()                       # Class instance object
#
# print(ty..(X))                       # Instance is instance of class
# # <class '__main__.C'>
# print(X.__class__)                  # Instance's class
# # <class '__main__.C'>
#
# print(ty..(C))                      # Class is instance of type
# # <class 'type'>
# print(C.__class__)                  # Class's class is type
# # <class 'type'>
#
#
# c_ C(o.. p..         # In 2.6 new-style classes,
#                               # classes have a class too
# X = C()
#
# print(ty..(X))
# # <class '__main__.C'>
# print(ty..(C))
# # <type 'type'>
#
# print(X.__class__)
# # <class '__main__.C'>
# print(C.__class__)
# # <type 'type'>
#
# c_ C p...                 # In 2.6 classic classes,
#                              # classes have no class themselves
# X = C()
#
# print(ty..(X))
# # <type 'instance'>
# print(ty..(C))
# # <type 'classobj'>
#
# print(X.__class__)
# # <class __main__.C at 0x005F85A0>
# print(C.__class__)
# # AttributeError: class C has no attribute '__class__'
#
