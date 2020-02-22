# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

# is a decorator
def verify_shape_type(func):
    def inner(self, shape):
        if not issubclass(type(shape), Shape) : print("%s is a type %s, the function need a Shape type" % (shape, type(shape))); exit(0)

        return func(self, shape)
    return inner

class Shape(object):
    """Abstract class
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self): raise NotImplementedError

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

class Square(Shape):

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side * self.side

class AreaCalculator(object):

    def __init__(self):
        self.shapes = []

    @verify_shape_type
    def set_shape(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area
        return total

if __name__ == '__main__':
    rectangle = Rectangle(12,22)
    square = Square(5)
    area_calculator = AreaCalculator()
    area_calculator.set_shape(rectangle)
    area_calculator.set_shape(square)

    print(area_calculator.total_area())
