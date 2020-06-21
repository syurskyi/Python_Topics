# -*- coding: utf-8 -*-

"""
Пример использования утиной типизации для работы с объектами, которые реализуют
определённый интерфейс.

В этом примере логически существует интерфейс "фигура", описываемый методом render,
хоть он и не описан отдельным абстрактным классом.
"""

# Классы из предыдущего примера

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
    shapes = [Square(5), IsoscelesRightTriangle(3), Rectangle(10, 3)]
    for shape in shapes:
        shape.render()


if __name__ == '__main__':
    main()
