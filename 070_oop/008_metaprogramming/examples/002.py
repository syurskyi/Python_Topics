# Abstract base classes (ABCs) enforce what derived classes implement particular methods from the base class.
#
# To understand how this works and why we should use it, let's take a look at an example that Van Rossum would enjoy.
# Let's say we have a Base class "MontyPython" with two methods (joke & punchline) that must be implemented by all derived classes.


class MontyPython:
    def joke(self):
        raise NotImplementedError()

    def punchline(self):
        raise NotImplementedError()


class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"

# When we instantiate an object and call it's two methods, we'll get an error (as expected) with the punchline() method.


sketch = ArgumentClinic()
sketch.punchline()


# NotImplementedError
# However, this still allows us to instantiate an object of the ArgumentClinic class without getting an error.
# In fact we don't get an error until we look for the punchline().
# This is avoided by using the Abstract Base Class (ABC) module. Let's see how this works with the same example:

from abc import ABCMeta, abstractmethod


class MontyPython(metaclass=ABCMeta):
    @abstractmethod
    def joke(self):
        pass


@abstractmethod
def punchline(self):
    pass


class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"


# This time when we try to instantiate an object from the incomplete class, we immediately get a TypeError!

c = ArgumentClinic()

# TypeError:
# "Can't instantiate abstract class ArgumentClinic with abstract methods punchline"
# In this case, it's easy to complete the class to avoid any TypeErrors:

class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"

    def punchline(self):
        return "Send in the constable!"
    
# This time when you instantiate an object it works!
