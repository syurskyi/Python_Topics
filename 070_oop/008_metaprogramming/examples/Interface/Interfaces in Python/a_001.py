# Interfaces in Python: Protocols and ABCs
#
# Python
#
# The idea of interface is really simple - it is the description of how an object behaves. An interface tells us
# what an object can do to play it’s role in a system. In object oriented programming, an interface is a set
# of publicly accessible methods on an object which can be used by other parts of the program to interact with
# that object. Interfaces set clear boundaries and help us organize our code better. In some langauges like Java,
# interfaces are part of the language syntax and strictly enforced. However, in Python, things are a little different.
# In this post, we will explore how interfaces can be implemented in Python.
# Informal Interfaces: Protocols / Duck Typing
#
# There’s no interface keyword in Python. The Java / C# way of using interfaces is not available here.
# In the dynamic language world, things are more implicit. We’re more focused on how an object behaves,
# rather than it’s type/class.
#
#     If it talks and walks like a duck, then it is a duck
#
# So if we have an object that can fly and quack like a duck, we consider it as a duck. This called “Duck Typing”.
# In runtime, instead of checking the type of an object, we try to invoke a method we expect the object to have.
# If it behaves the way we expected, we’re fine and move along. But if it doesn’t, things might blow up. To be safe,
# we often handle the exceptions in a try..except block or use hasattr to check if an object has the specific method.
#
# In the Python world, we often hear “file like object” or “an iterable” - if an object has a read method,
# it can be treated as a file like object, if it has an __iter__ magic method, it is an iterable.
# So any object, regardless of it’s class/type, can conform to a certain interface just by implementing the expected
# behavior (methods). These informal interfaces are termed as protocols. Since they are informal, they can not be
# formally enforced. They are mostly illustrated in the documentations or defined by convention.
# All the cool magic methods you have heard about - __len__, __contains__, __iter__ - they all help an object
# to conform to some sort of protocols.


class Team:
    def __init__(self, members):
        self.__members = members

    def __len__(self):
        return len(self.__members)

    def __contains__(self, member):
        return member in self.__members


justice_league_fav = Team(["batman", "wonder woman", "flash"])

# Sized protocol
print(len(justice_league_fav))

# Container protocol
print("batman" in justice_league_fav)
print("superman" in justice_league_fav)
print("cyborg" not in justice_league_fav)

# In our above example, by implementing the __len__ and __contains__ method, we can now directly use the len function
# on a Team instance and check for membership using the in operator. If we add the __iter__ method to implement
# the iterable protocol, we would even be able to do something like:


for member in justice_league_fav:
    print(member)

# Without implementing the __iter__ method, if we try to iterate over the team, we will get an error like:
#
# TypeError: 'Team' object is not iterable
#
# So we can see that protocols are like informal interfaces. We can implement a protocol by implementing
# the methods expected by it.
# Formal Interfaces: ABCs
#
# While protocols work fine in many cases, there are situations where informal interfaces or duck typing in general
# can cause confusion. For example, a Bird and Aeroplane both can fly(). But they are not the same thing even
# if they implement the same interfaces / protocols. Abstract Base Classes or ABCs can help solve this issue.
#
# The concept behind ABCs is simple - we define base classes which are abstract in nature. We define certain methods
# on the base classes as abstract methods. So any objects deriving from these bases classes are forced
# to implement those methods. And since we’re using base classes, if we see an object has our class as a base class,
# we can say that this object implements the interface. That is now we can use types to tell if an object implements
# a certain interface. Let’s see an example.

import abc

class Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

# There’s the abc module which has a metaclass named ABCMeta. ABCs are created from this metaclass.
# So we can either use it directly as the metaclass of our ABC
# (something like this - class Bird(metaclass=abc.ABCMeta):) or we can subclass from the abc.ABC class which has
# the abc.ABCMeta as it’s metaclass already.
#
# Then we have to use the abc.abstractmethod decorator to mark our methods abstract. Now if any class derives
# from our base Bird class, it must implement the fly method too. The following code would fail:

class Parrot(Bird):
    pass

p = Parrot()

# We see the following error:
#
# TypeError: Can't instantiate abstract class Parrot with abstract methods fly
#
# Let’s fix that:


class Parrot(Bird):
    def fly(self):
        print("Flying")


p = Parrot()

# Also note:

isinstance(p, Bird)
# True

# Since our parrot is recognized as an instance of Bird ABC, we can be sure from it’s type that it definitely
# implements our desired interface.
#
# Now let’s define another ABC named Aeroplane like this:

class Aeroplane(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass


class Boeing(Aeroplane):
    def fly(self):
        print("Flying!")

b = Boeing()

# Now if we compare:


isinstance(p, Aeroplane)
# False

isinstance(b, Bird)
# False

# We can see even though both objects have the same method fly but we can now differentiate easily which one implements
# the Bird interface and which implements the Aeroplane interface.
#
# We saw how we can create our own, custom ABCs. But it is often discouraged to create custom ABCs and rather
# use/subclass the built in ones. The Python standard library has many useful ABCs that we can easily reuse.
# We can get a list of useful built in ABCs in the
# collections.abc module - https://docs.python.org/3/library/collections.abc.html#module-collections.abc.
# Before writing your own, please do check if there’s an ABC for the same purpose in the standard library.
# ABCs and Virtual Subclass
#
# We can also register a class as a virtual subclass of an ABC. In that case, even if that class doesn’t subclass
# our ABC, it will still be treated as a subclass of the ABC (and thus accepted to have implemented the interface).
# Example codes will be able to demonstrate this better:

@Bird.register
class Robin:
    pass

r = Robin()

# And then:

issubclass(Robin, Bird)
# True

isinstance(r, Bird)
# True


# In this case, even if Robin does not subclass our ABC or define the abstract method, we can register
# it as a Bird. issubclass and isinstance behavior can be overloaded by adding two relevant magic methods.
#