#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 7/8/2018

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Shape(metaclass=ABCMeta):
    """shape"""

    def __init__(self, color):
        self._color = color

    @abstractmethod
    def getShapeType(self):
        pass

    def getShapeInfo(self):
        return self._color.getColor() + "of" + self.getShapeType()


class Rectange(Shape):
    """rectangle"""

    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return "rectangle"

class Ellipse(Shape):
    """oval"""

    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return "oval"

class Color(metaclass=ABCMeta):
    """colour"""

    @abstractmethod
    def getColor(self):
        pass


class Red(Color):
    """red"""

    def getColor(self):
        return "red"


class Green(Color):
    """green"""

    def getColor(self):
        return "green"

# Version 2.0
#=======================================================================================================================
# Code framework
#==============================


# Framework-based implementation
#==============================


# Test
#=======================================================================================================================

def Shap():
    redRect = Rectange(Red())
    print(redRect.getShapeInfo())
    greenRect = Rectange(Green())
    print(greenRect.getShapeInfo())

    redEllipse = Ellipse(Red())
    print(redEllipse.getShapeInfo())
    greenEllipse = Ellipse(Green())
    print(greenEllipse.getShapeInfo())


Shap()