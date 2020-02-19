# An abstract class can be considered as a blueprint for other classes, allows you to create a set of methods
# hat must be created within any child classes built from your abstract class. A class which contains one or abstract
# methods is called an abstract class. An abstract method is a method that has declaration but not has
# any implementation. Abstract classes are not able to instantiated and it needs subclasses to provide implementations
# for those abstract methods which are defined in abstract classes. While we are designing large functional units
# we use an abstract class. When we want to provide a common implemented functionality for all implementations
# of a component, we use an abstract class. Abstract classes allow partially to implement classes when it completely
# implements all methods in a class, then it is called interface.
#
# Why use Abstract Base Classes :
# Abstract classes allow you to provide default functionality for the subclasses. Compared to interfaces abstract
# classes can have an implementation. By defining an abstract base class, you can define a common
# Application Program Interface(API) for a set of subclasses. This capability is especially useful in situations where
# a third-party is going to provide implementations, such as with plugins in an application, but can also help you
# when working on a large team or with a large code-base where keeping all classes in your head at the same time
# is difficult or not possible.
#
# How Abstract Base classes work :
# In python by default, it is not able to provide abstract classes, but python comes up with a module which provides
# the base for defining Abstract Base classes(ABC) and that module name is ABC. ABC works by marking methods
# f the base class as abstract and then registering concrete classes as implementations of the abstract base.
# A method becomes an abstract by decorated it with a keyword @abstractmethod. For Example

# Python program showing
# abstract base class work

from abc import ABC, abstractmethod


class Polygon(ABC):

    # abstract method
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

    # Driver code


R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()


# I have 3 sides
# I have 4 sides
# I have 5 sides
# I have 6 sides
