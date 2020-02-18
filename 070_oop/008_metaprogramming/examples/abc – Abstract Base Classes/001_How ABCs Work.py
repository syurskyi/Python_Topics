# abc works by marking methods of the base class as abstract, and then registering concrete classes as implementations
# of the abstract base. If your code requires a particular API, you can use issubclass() or isinstance() to check
# an object against the abstract class.
#
# Let’s start by defining an abstract base class to represent the API of a set of plugins for saving and loading data.

import abc

class PluginBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""
        return

# Registering a Concrete Class
#
# There are two ways to indicate that a concrete class implements an abstract: register the class with the abc or subclass directly from the abc.

import abc
from abc_base import PluginBase

class RegisteredImplementation(object):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

PluginBase.register(RegisteredImplementation)

if __name__ == '__main__':
    print('Subclass:', issubclass(RegisteredImplementation, PluginBase))
    print('Instance:', isinstance(RegisteredImplementation(), PluginBase))

# In this example the PluginImplementation is not derived from PluginBase, but is registered as implementing the PluginBase API.
#
# $ python abc_register.py
#
# Subclass: True
# Instance: True