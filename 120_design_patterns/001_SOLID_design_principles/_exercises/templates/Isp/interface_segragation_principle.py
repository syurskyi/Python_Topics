# Interface Segregation Principle (ISP)

# No client should be forced to depend on methods it doesn't use


from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class Color(Enum):
    RED = "red"
    GREEN = "green"
    ORANGE = "orange"
    BLUE = "blue"


class ColoredShape(ABC):
    def __init__(self, color: Color):
        self.color = color


class ShapeWithArea(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        pass


class OpenCircle(ColoredShape):
    def __str__(self):
        return f"{self.color.value} circle"


class Rectangle(ShapeWithArea, ColoredShape):
    def __init__(self, color: Color, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    def __str__(self):
        return f"{self.color.value} rectangle with an area of {self.area}"


class Square(ShapeWithArea, ColoredShape):
    def __init__(self, color: Color, side: float):
        super().__init__(color)
        self.side = side

    @property
    def area(self) -> float:
        return self.side * self.side

    def __str__(self):
        return f"{self.color.value} square with an area of {self.area}"


def blue_filter(shapes: List[ColoredShape]):
    for shape in shapes:
        if shape.color == Color.BLUE:
            yield shape


def area_filter(shapes: List[ShapeWithArea], max_area: float):
    for shape in shapes:
        if shape.area <= max_area:
            yield shape


if __name__ == "__main__":
    rectangle = Rectangle(Color.BLUE, 3.0, 2.0)
    print(rectangle)

    square = Square(Color.GREEN, 3.0)
    print(square)

    open_circle = OpenCircle(Color.BLUE)
    print(open_circle)

    blue_shapes = blue_filter([rectangle, square, open_circle])
    for blue_shape in blue_shapes:
        print(blue_shape)
