# -*- coding: utf-8 -*-

# В этом примере показано использование специального метода
# __new__ для реализации такого шаблона проектирования как
# Одиночка (Singleton).
#
# Одиночка — порождающий шаблон проектирования, гарантирующий,
# что данный класс имеет только один экземпляр.


class Singleton:
    _instance = None  # атрибут, хранящий экземпляр класса

    def __new__(cls, *args, **kwargs):
        """
        Метод __new__ вызывается при создании экземпляра класса.
        """

        # Если экземпляр ещё не создан, то создаём его
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)

        # Возвращаем существующий экземпляр
        return cls._instance

    def __init__(self):
        self.value = 8


obj1 = Singleton()
print(obj1.value)

obj2 = Singleton()
obj2.value = 42
print(obj1.value)