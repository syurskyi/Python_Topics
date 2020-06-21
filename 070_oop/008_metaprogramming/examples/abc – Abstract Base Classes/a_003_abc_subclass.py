# abc_subclass.py

# Implementation Through Subclassing
# Subclassing directly from the base avoids the need to register the class explicitly.

import abc
from a_001_abc_base import PluginBase


class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('Subclass:', issubclass(SubclassImplementation,
                                  PluginBase))
    print('Instance:', isinstance(SubclassImplementation(),
                                  PluginBase))


# $ python3 abc_subclass.py
#
# Subclass: True
# Instance: True


# In this case, normal Python class management features are used to recognize SubclassImplementation as implementing
# the abstract PluginBase.


# python 2

# import abc
# from abc_base import PluginBase
#
#
# class SubclassImplementation(PluginBase):
#
#     def load(self, input):
#         return input.read()
#
#     def save(self, output, data):
#         return output.write(data)
#
#
# if __name__ == '__main__':
#     print 'Subclass:', issubclass(SubclassImplementation, PluginBase)
#     print 'Instance:', isinstance(SubclassImplementation(), PluginBase)
