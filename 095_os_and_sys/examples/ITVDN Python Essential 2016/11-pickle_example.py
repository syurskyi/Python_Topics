"""Пример сериализации при помощи pickle"""

import os.path
import pickle
import reprlib


class Person(object):
    """Класс, описывающий человека"""

    def __init__(self, name, age, sibling=None):
        """Конструктор класса.

        Параметры:
            name    -- имя
            age     -- возраст
            sibling -- брат или сестра
        """
        self.name = name
        self.age = age
        self.sibling = sibling

    # Декоратор reprlib.recursive_repr(fillvalue='...') отслеживает рекурсивные
    # вызовы метода __repr__ и не даёт ему войти в бесконечную рекурсию,
    # возвращая fillvalue вместо вызовов данного метода, которые ещё не
    # завершены.
    @reprlib.recursive_repr()
    def __repr__(self):
        """Строковое представление объекта"""
        return 'Person({name!r}, {age!r}, {sibling!r})'.format(**self.__dict__)


def write_data(filename):
    """Функция создания и записи данных"""

    james = Person('James', 20)
    julia = Person('Julia', 21)
    james.sibling = julia  # создание циклических ссылок
    julia.sibling = james

    # Сериализация списка объектов
    with open(filename, 'wb') as file:  # 'wb' -- запись бинарного файла
        pickle.dump([james, julia], file)


def read_data(filename):
    """Функция чтения и вывода данных на экран"""

    # Десериализация
    with open(filename, 'rb') as file:
        data = pickle.load(file)

    # Вывод в консоль
    print(data)


if __name__ == '__main__':
    filename = os.path.join('data', 'example11.pkl')
    write_data(filename)
    read_data(filename)
