# -*- coding: utf-8 -*-

class MyClass:
    def __init__(self, value):
        self.__var = value
    @property
    def v(self):                       # Чтение
        return self.__var
    @v.setter
    def v(self, value):                # Запись
        self.__var = value
    @v.deleter
    def v(self):                       # Удаление
        del self.__var
c = MyClass(5)
c.v = 35                               # Запись
print(c.v)                             # Чтение
del c.v                                # Удаление
