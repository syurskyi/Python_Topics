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
    def area(self) -> None:
        pass


class OpenCircle(ColoredShape):
    def __str__(self):
        return f'{self.color.value}, circle'


class Rectangle(ShapeWithArea, ColoredShape):
    def __init__(self, color: ColoredShape, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    def __str__(self):
        return f'{self.color.value} rectangle with an area of {self.area}'


class Square(ShapeWithArea, ColoredShape):
    def __init__(self, color: ColoredShape, side: float):
        super().__init__(color)
        self.side = side

    @property
    def area(self) -> float:
        return self.side * self.side

    def __str__(self):
        return f'{self.color.value} square with an area of {self.area}'


def blue_filter(shapes: List[ColoredShape]):
    for shape in shapes:
        if shape.color == Color.BLUE
            yield shape


___ area_filter shapes L..|S.. max_area ?
    ___ shape __ ?
        __ ?.a.. <_ m..
            y.. ?


__ ______ __ ______
    rectangle _ R.. C__.B.. 3.0, 2.0
    print ?

    square _ S.. C__.G.. 3.0
    print ?

    open_circle _ O.. C__.B..
    print ?

    blue_shapes = b_f.. ?  ?  ?
    ___ blue_shape __ ?
        print ?
