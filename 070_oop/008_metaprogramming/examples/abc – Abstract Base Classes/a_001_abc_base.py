# abc_base.py

# Why use Abstract Base Classes?
# Abstract base classes are a form of interface checking more strict than individual hasattr() checks for particular
# methods. By defining an abstract base class, a common API can be established for a set of subclasses.
# This capability is especially useful in situations where someone less familiar with the source for an application is
# going to provide plug-in extensions, but can also help when working on a large team or with a large code-base
# where keeping track of all of the classes at the same time is difficult or not possible.
#
# How ABCs Work
# abc works by marking methods of the base class as abstract, and then registering concrete classes as implementations
# of the abstract base. If an application or library requires a particular API, issubclass() or isinstance()
# can be used to check an object against the abstract class.
#
# To start, define an abstract base class to represent the API of a set of plug-ins for saving and loading data.
# Set the metaclass for the new base class to ABCMeta, and use decorators to establish the public API for the class.
# The following examples use abc_base.py.

import abc


class PluginBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source
        and return an object.
        """

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""


# python 2

# import abc
#
#
# class PluginBase(object):
#     __metaclass__ = abc.ABCMeta
#
#     @abc.abstractmethod
#     def load(self, input):
#         """Retrieve data from the input source and return an object."""
#         return
#
#     @abc.abstractmethod
#     def save(self, output, data):
#         """Save the data object to the output."""
#         return
