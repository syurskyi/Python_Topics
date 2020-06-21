# # abc_abstractproperty_rw.py
#
# # Abstract read-write properties can also be defined.
#
#
# ______ a..
#
#
# c_ Base a..
#
#     ??
#     ??.?
#     def value
#         r_ 'Should never reach here'
#
#     ??.?
#     ??.?
#     ___ value  new_value
#         r_
#
#
# c_ PartialImplementation ?
#
#     ??
#     ___ value
#         r_ 'Read-only'
#
#
# c_ Implementation ?
#
#     _value = 'Default value'
#
#     ??
#     ___ value
#         r_ _?
#
#     ??.?
#     ___ value  new_value
#         _v.. _ ?
#
#
# ___
#     b = B..
#     print('Base.value:' ?.v..
# _______ E.. __ err
#     print('ERROR:', st. ?
#
# p = P..
# print('PartialImplementation.value:', ?.v..
#
# ___
#     ?.v.. = 'Alteration'
#     print('PartialImplementation.value:', ?.v...
#     _______ E.. __ err
#     print('ERROR:', st. ?
#
# i = I..
# print('Implementation.value:', ?.v...
#
# ?.v.. = 'New value'
# print('Changed value:', ?.v..
#
# # The concrete property must be defined the same way as the abstract property, as either read-write or read-only.
# # Overriding a read-write property in PartialImplementation with one that is read-only leaves the property read-only
# # the property's setter method from the base class is not reused.
#
# # $ python3 abc_abstractproperty_rw.py
# #
# # ERROR: Can't instantiate abstract class Base with abstract
# # methods value
# # PartialImplementation.value: Read-only
# # ERROR: can't set attribute
# # Implementation.value: Default value
# # Changed value: New value

# # python 2
#
# # import abc
# #
# # class Base(object):
# #     __metaclass__ = abc.ABCMeta
# #
# #     def value_getter(self):
# #         return 'Should never see this'
# #
# #     def value_setter(self, newvalue):
# #         return
# #
# #     value = abc.abstractproperty(value_getter, value_setter)
# #
# #
# # class PartialImplementation(Base):
# #
# #     @abc.abstractproperty
# #     def value(self):
# #         return 'Read-only'
# #
# #
# # class Implementation(Base):
# #
# #     _value = 'Default value'
# #
# #     def value_getter(self):
# #         return self._value
# #
# #     def value_setter(self, newvalue):
# #         self._value = newvalue
# #
# #     value = property(value_getter, value_setter)
# #
# #
# # try:
# #     b = Base()
# #     print 'Base.value:', b.value
# # except Exception, err:
# #     print 'ERROR:', str(err)
# #
# # try:
# #     p = PartialImplementation()
# #     print 'PartialImplementation.value:', p.value
# # except Exception, err:
# #     print 'ERROR:', str(err)
# #
# # i = Implementation()
# # print 'Implementation.value:', i.value
# #
# # i.value = 'New value'
# # print 'Changed value:', i.value
