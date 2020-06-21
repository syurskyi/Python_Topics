# -*- coding: utf-8 -*-

"""
Пример использования полиморфизма
"""

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


def main():
    shapes = [Square(5), IsoscelesRightTriangle(3), Square(7), IsoscelesRightTriangle(8)]
    for shape in shapes:
        shape.render()


if __name__ == '__main__':
    main()
