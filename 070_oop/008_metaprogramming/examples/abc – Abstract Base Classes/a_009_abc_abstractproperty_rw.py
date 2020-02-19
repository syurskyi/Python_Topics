# abc_abstractproperty_rw.py

# Abstract read-write properties can also be defined.


import abc


class Base(abc.ABC):

    @property
    @abc.abstractmethod
    def value(self):
        return 'Should never reach here'

    @value.setter
    @abc.abstractmethod
    def value(self, new_value):
        return


class PartialImplementation(Base):

    @property
    def value(self):
        return 'Read-only'


class Implementation(Base):

    _value = 'Default value'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


try:
    b = Base()
    print('Base.value:', b.value)
except Exception as err:
    print('ERROR:', str(err))

p = PartialImplementation()
print('PartialImplementation.value:', p.value)

try:
    p.value = 'Alteration'
    print('PartialImplementation.value:', p.value)
except Exception as err:
    print('ERROR:', str(err))

i = Implementation()
print('Implementation.value:', i.value)

i.value = 'New value'
print('Changed value:', i.value)

# The concrete property must be defined the same way as the abstract property, as either read-write or read-only.
# Overriding a read-write property in PartialImplementation with one that is read-only leaves the property read-only
# the property's setter method from the base class is not reused.

# $ python3 abc_abstractproperty_rw.py
#
# ERROR: Can't instantiate abstract class Base with abstract
# methods value
# PartialImplementation.value: Read-only
# ERROR: can't set attribute
# Implementation.value: Default value
# Changed value: New value
