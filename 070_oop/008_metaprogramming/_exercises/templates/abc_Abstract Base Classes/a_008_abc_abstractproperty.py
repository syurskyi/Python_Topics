# # abc_abstractproperty.py
#
# # Abstract Properties
# # If an API specification includes attributes in addition to methods, it can require the attributes in concrete classes
# # by combining abstractmethod() with property().
#
#
# ______ a..
#
#
# c_ Base a..
#
#     ??
#     ??.?
#     ___ value
#         r_ 'Should never reach here'
#
#     ??
#     ??.?
#     ___ constant
#         r_ 'Should never reach here'
#
#
# c_ Implementation ?
#
#     ??
#     ___ value
#         r_ 'concrete property'
#
#     constant = 'set by a class attribute'
#
#
# ___
#     b = B..
#     print('Base.value:' ?.v..
# _______ E.. __ err:
#     print('ERROR:', st. ?
#
# i = I..
# print('Implementation.value   :' ?.v..
# print('Implementation.constant:' ?.c..
#
#
# # The Base class in the example cannot be instantiated because it has only an abstract version of the property getter
# # methods for value and constant. The value property is given a concrete getter in Implementation and constant is
# # defined using a class attribute.
#
# # $ python3 abc_abstractproperty.py
# #
# # ERROR: Can't instantiate abstract class Base with abstract
# # methods constant, value
# # Implementation.value   : concrete property
# # Implementation.constant: set by a class attribute

# # python 2
#
# # import abc
# #
# # class Base(object):
# #     __metaclass__ = abc.ABCMeta
# #
# #     @abc.abstractproperty
# #     def value(self):
# #         return 'Should never get here'
# #
# #
# # class Implementation(Base):
# #
# #     @property
# #     def value(self):
# #         return 'concrete property'
# #
# #
# # try:
# #     b = Base()
# #     print 'Base.value:', b.value
# # except Exception, err:
# #     print 'ERROR:', str(err)
# #
# # i = Implementation()
