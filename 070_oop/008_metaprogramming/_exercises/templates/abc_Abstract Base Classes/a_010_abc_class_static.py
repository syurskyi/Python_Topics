# # abc_class_static.py
#
# # Abstract Class and Static Methods
# # Class and static methods can also be marked as abstract.
#
# ______ a..
#
#
# c_ Basea..
#
#     ??
#     ??.?
#     def factory(cls, *args):
#         r_ cls()
#
#     ??
#     ??.?
#     ___ const_behavior
#         r_ 'Should never reach here'
#
#
# c_ Implementation ?
#
#     ___ do_something ?
#         p..
#
#     ??
#     ___ factory ___ $
#         obj = ___ $
#         ?.d..
#         r_ ?
#
#     ??
#     def const_behavior
#         r_ 'Static behavior differs'
#
#
# ___
#     o = B__.f..
#     print('Base.value:' ?.c..
# ______ Exception  err
#     print('ERROR:', st. ?
#
# i = I__.f..
# print('Implementation.const_behavior :' ?.c..
#
# # Although the class method is invoked on the class rather than an instance, it still prevents the class from being
# # instantiated if it is not defined.
#
# # $ python3 abc_class_static.py
# #
# # ERROR: Can't instantiate abstract class Base with abstract
# # methods const_behavior, factory
# # Implementation.const_behavior : Static behavior differs
