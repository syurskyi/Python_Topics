#=======================================================================================================================
import logging
# Introduce logging module to record exceptions

class Pigment:
    """pigment"""

    def __init__(self, color):
        self.__color = color
        self.__user = ""

    def getColor(self):
        return self.__color

    def setUser(self, user):
        self.__user = user
        return self

    def showInfo(self):
        print("%s get %s color pigment"  % (self.__user, self.__color) )

class PigmengFactory:
    """Data Factory Class"""

    def __init__(self):
        self.__sigmentSet = {
            "red": Pigment("red"),
            "yellow": Pigment("yellow"),
            "blue": Pigment("blue"),
            "green": Pigment("green"),
            "purple": Pigment("purple"),
        }

    def getPigment(self, color):
        pigment = self.__sigmentSet.get(color)
        if pigment is None:
            logging.error("No %s Color！", color)
        return pigment


# Version 2.0
#=======================================================================================================================
# Code framework
#==============================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Flyweight(metaclass=ABCMeta):
    """Flyweight Class"""

    @abstractmethod
    def operation(self, extrinsicState):
        pass

class FlyweightImpl(Flyweight):
    """Concrete implementation class of Flyweight class"""

    def __init__(self, color):
        self.__color = color

    def operation(self, extrinsicState):
        print("%s Get %s Color pigment" % (extrinsicState, self.__color))

class FlyweightFactory:
    """Flyweight Factory"""

    def __init__(self):
        self.__flyweights = {}

    def getFlyweight(self, key):
        pigment = self.__flyweights.get(key)
        if pigment is None:
            pigment = FlyweightImpl(key)
        return pigment

# Framework-based implementation
#==============================


# Test
#=======================================================================================================================
def Pigment():
    factory = PigmengFactory()
    pigmentRed = factory.getPigment("red").setUser("Dream team")
    pigmentRed.showInfo()
    pigmentYellow = factory.getPigment("yellow").setUser("Dream team")
    pigmentYellow.showInfo()
    pigmentBlue1 = factory.getPigment("blue").setUser("Dream team")
    pigmentBlue1.showInfo()
    pigmentBlue2 = factory.getPigment("blue").setUser("Peace corps")
    pigmentBlue2.showInfo()


def Flyweight():
    factory = FlyweightFactory()
    pigmentRed = factory.getFlyweight("red")
    pigmentRed.operation("Dream team")
    pigmentYellow = factory.getFlyweight("yellow")
    pigmentYellow.operation("Dream team")
    pigmentBlue1 = factory.getFlyweight("blue")
    pigmentBlue1.operation("Dream team")
    pigmentBlue2 = factory.getFlyweight("blue")
    pigmentBlue2.operation("Peace corps")


# print("Blue1:" + str(id(pigmentBlue1)) + ", Bule2:" + str(id(pigmentBlue2))
#       + ", Blue1==Blue2:" + str(pigmentBlue1 == pigmentBlue2))



# Pigment()
Flyweight()
