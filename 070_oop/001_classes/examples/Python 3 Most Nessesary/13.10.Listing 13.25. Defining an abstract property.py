# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
class MyClass1(metaclass=ABCMeta):
    def __init__(self, value):
        self.__var = value
    @property
    @abctractmethod
    def v(self):                       # Чтение
        return self.__var
    @v.setter
    @abctractmethod
    def v(self, value):                # Запись
        self.__var = value
    @v.deleter
    @abctractmethod
    def v(self):                       # Удаление
        del self.__var