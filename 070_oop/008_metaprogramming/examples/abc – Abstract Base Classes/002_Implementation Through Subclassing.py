# Implementation Through Subclassing
#
# By subclassing directly from the base, we can avoid the need to register the class explicitly.
#
import abc
from abc_base import PluginBase

class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

if __name__ == '__main__':
    print('Subclass:', issubclass(SubclassImplementation, PluginBase))
    print('Instance:', isinstance(SubclassImplementation(), PluginBase))

# In this case the normal Python class management is used to recognize PluginImplementation as implementing the abstract PluginBase.
#
# $ python abc_subclass.py
#
# Subclass: True
# Instance: True