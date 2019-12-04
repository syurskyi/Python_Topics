# -*- coding: utf-8 -*-

# Так как классы тоже являются объектами, то помимо атрибутов-функций
# они могут иметь и собственные методы. Для создания методов класса
# используется декоратор classmethod. В таких методах первый параметр
# принято называть не self, а cls.
#
# Методы класса обычно используются в двух случаях:
# •	для создания фабричных методов, которые создают
#   экземпляры данного класса альтернативными способами;
# •	статические методы, вызывающие статические методы:
#   поскольку данный класс передаётся как первый аргумент функции,
#   не нужно вручную указывать имя класса для вызова статического метода.


class Rectangle:
    """
    Класс, описывающий прямоугольник
    """

    def __init__(self, side_a, side_b):
        """
        Конструктор класса
        :param side_a: первая сторона
        :param side_b: вторая сторона
        """
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self):
        """
        Метод, который возвращает строковое представление объекта
        """
        return 'Rectangle(%.1f, %.1f)' % (self.side_a, self.side_b)


class Circle:
    """
    Класс, описывающий окружность
    """

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return 'Circle(%.1f)' % self.radius

    @classmethod
    def from_rectangle(cls, rectangle):
        """
        Мы используем метод класса в качестве фабричного метода,
        который создаёт экземпляр класса Circle из экземпляра
        класса Rectangle как окружность, вписанную в данный
        прямоугольник.

        :param rectangle: Rectangle instance
        :return: Circle instance
        """
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return cls(radius)


def main():
    rectangle = Rectangle(3, 4)
    print(rectangle)
    circle1 = Circle(1)
    print(circle1)
    circle2 = Circle.from_rectangle(rectangle)
    print(circle2)


if __name__ == '__main__':
    main()