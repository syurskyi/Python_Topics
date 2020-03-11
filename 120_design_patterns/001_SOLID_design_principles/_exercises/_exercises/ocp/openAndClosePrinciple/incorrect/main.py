# -*- coding: utf-8 -*-

class Rectangle(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(object):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class AreaCalculator(object):

    def __init__(self):
        self.rectangle = Rectangle(12,22)
        self.square = Square(5)

    def total_area(self):
        total = self.rectangle.area() + self.square.area()
        return total

if __name__ == '__main__':
    area_calculator = AreaCalculator()
    print(area_calculator.total_area())
