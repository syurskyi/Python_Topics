# Abstract Class Instantiation :
# Abstract classes are incomplete because they have methods which have no body. If python allows creating an object
# for abstract classes then using that object if anyone calls the abstract method, but there is no actual implementation
# o invoke. So we use an abstract class as a template and according to the need we extend it and build on it before
# we can use it. Due to the fact, an abstract class is not a concrete class, it cannot be instantiated.
# When we create an object for the abstract class it raises an error.

# Python program showing
# abstract class cannot
# be an instantiation
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


c = Animal()

# Output:
#
# Traceback (most recent call last):
#   File "/home/ffe4267d930f204512b7f501bb1bc489.py", line 19, in
#     c=Animal()
# TypeError: Can't instantiate abstract class Animal with abstract methods move
