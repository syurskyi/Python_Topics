# abc_abc_base.py

import abc

# Forgetting to set the metaclass properly means the concrete implementations do not have their APIs enforced.
# To make it easier to set up the abstract class properly, a base class is provided that sets the metaclass
# automatically.


class PluginBase(abc.ABC):

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source
        and return an object.
        """

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""


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


# Subclass: True
# Instance: True

# To create a new abstract class, simply inherit from ABC.
