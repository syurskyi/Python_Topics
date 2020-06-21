# Liskov Substitution Principle (LSP)

# Functions that use references to base classes must be able to use any object of derived classes without knowing it.

# Consequence: Sometimes something "is a" in the real world but should not be an "is a" in the code


class Rectangle:
    def __init__(self, name: str, width: float, height: float):
        self.name = name
        self._height = height
        self._width = width

    def __str__(self):
        return f"{self.name}: {self._width}x{self._height}"

    def double_height(self):
        self._height *= 2

    def double_width(self):
        self._width *= 2

    @property
    def is_square(self) -> bool:
        return self._width == self._height


class Square(Rectangle):
    def __init__(self, name: str, side: float):
        super().__init__(name, side, side)

    def double_height(self):
        self._height *= 2
        self._width *= 2

    def double_width(self):
        self._width *= 2
        self._height *= 2


def double_size(rectangle: Rectangle) -> None:
    rectangle.double_height()
    rectangle.double_width()


if __name__ == "__main__":
    rectangle = Rectangle("My Rectangle", 3, 2)
    print(rectangle)

    # rectangle.double_height()
    double_size(rectangle)
    print(rectangle)

    square = Square("My Square", 3)
    print(square)

    # square.double_height()
    double_size(square)
    print(square)
