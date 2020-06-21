#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Coffee(metaclass=ABCMeta):
    """coffee"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def getTaste(self):
        pass


class LatteCaffe(Coffee):
    """latte"""

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "Gentle and mellow"

class MochaCoffee(Coffee):
    """Mocha"""

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "Silky and mellow"

class Coffeemaker:
    """咖啡机"""

    @staticmethod
    def makeCoffee(coffeeBean):
        "Define a static method with the staticmethod decorator"
        if(coffeeBean == "Latte coffee beans"):
            coffee = LatteCaffe("latte")
        elif(coffeeBean == "Mocha coffee beans"):
            coffee = MochaCoffee("Mocha")
        else:
            raise ValueError("Unsupported parameters %s" % coffeeBean)
        return coffee



# Version 2.0
#=======================================================================================================================
# Code framework
#==============================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
from enum import Enum
# Python3.4 Enum syntax is supported afterwards

class PenType(Enum):
    """Brush type"""
    PenTypeLine = 1
    PenTypeRect = 2
    PenTypeEllipse = 3


class Pen(metaclass=ABCMeta):
    """brush"""

    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def getType(self):
        pass

    def getName(self):
        return self.__name


class LinePen(Pen):
    """Straight brush"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeLine

class RectanglePen(Pen):
    """Rectangular brush"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeRect


class EllipsePen(Pen):
    """Oval brush"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeEllipse


class PenFactory:
    """Brush factory class"""

    def __init__(self):
        "Define a dictionary (key: PenType, value: Pen) to store objects, and ensure that there will only be one object of each type"
        self.__pens = {}

    def getSingleObj(self, penType, name):
        """Get unique instance of object"""


    def createPen(self, penType):
        """Create brush"""
        if (self.__pens.get(penType) is None):
            # If the object does not exist, an object is created and stored in the dictionary
            if penType == PenType.PenTypeLine:
                pen = LinePen("Straight brush")
            elif penType == PenType.PenTypeRect:
                pen = RectanglePen("Rectangular brush")
            elif penType == PenType.PenTypeEllipse:
                pen = EllipsePen("Oval brush")
            else:
                pen = Pen("")
            self.__pens[penType] = pen
        # Otherwise return the object in the dictionary directly
        return self.__pens[penType]


# Framework-based implementation
#==============================


# Test
#=======================================================================================================================
def testCoffeeMaker():
    latte = Coffeemaker.makeCoffee("Latte coffee beans")
    print("%s Ready for you, taste: %s. Please enjoy slowly!" % (latte.getName(), latte.getTaste()) )
    mocha = Coffeemaker.makeCoffee("Mocha coffee beans")
    print("%s is ready for you, taste: %s. Please enjoy slowly!" % (mocha.getName(), mocha.getTaste()))


def testPenFactory():
    factory = PenFactory()
    linePen = factory.createPen(PenType.PenTypeLine)
    print("created %s，Object id: %s， Types of:%s" % (linePen.getName(), id(linePen), linePen.getType()) )
    rectPen = factory.createPen(PenType.PenTypeRect)
    print("created %s，Object id: %s， Types of: %s" % (rectPen.getName(), id(rectPen), rectPen.getType()) )
    rectPen2 = factory.createPen(PenType.PenTypeRect)
    print("created %s，Object id: %s， Types of:%s" % (rectPen2.getName(), id(rectPen2), rectPen2.getType()) )
    ellipsePen = factory.createPen(PenType.PenTypeEllipse)
    print("created %s，Object id: %s， Types of: %s" % (ellipsePen.getName(), id(ellipsePen), ellipsePen.getType()) )


# testCoffeeMaker()
testPenFactory()