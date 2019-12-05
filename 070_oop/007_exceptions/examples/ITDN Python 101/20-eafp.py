# -*- coding: utf-8 -*-

"""
Пример проверки реализации объектом необходимого интерфейса
с использованием стиля Easier to Ask for Forgiveness that Permission
(рекоммендуется).
"""

# Классы равнобедренных фигур

class IsoscelesShape(object):
    def __init__(self, side):
        self.side = side

    def render(self):
        print(self)
        self.draw()
        print()

    def __str__(self):
        return 'Abstract figure object'

    def draw(self):
        pass


class Square(IsoscelesShape):
    def draw(self):
        for _ in range(self.side):
            print('*' * self.side)

    def __str__(self):
        return 'Square with a side of {!r}'.format(self.side)


class IsoscelesRightTriangle(Square):
    def draw(self):
        for i in range(1, self.side + 1):
            print('*' * i)

    def __str__(self):
        return 'Isosceles right triangle with a side of {!r}'.format(self.side)


# Класс, который не наследуется от классов равнобедренных фигур
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def render(self):
        print('Rectangle with sides {!r} and {!r}'.format(self.width, self.height))
        print('\n'.join(['*' * self.width] * self.height))
        print()


def main():
    shapes = [Square(5), IsoscelesRightTriangle(3), Rectangle(10, 3), 42]
    for shape in shapes:
        try:
            shape.render()
        except AttributeError:
            print(repr(shape), 'is not a shape.')


if __name__ == '__main__':
    main()
