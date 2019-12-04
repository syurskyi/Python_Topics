# -*- coding: utf-8 -*-

"""
isinstance(obj, cls) проверяет, является ли obj экземпляром класса cls
или класса, который является наследником класса cls
"""

print(isinstance(8, int))  # True
print(isinstance('str', int))  # False
print(isinstance(True, bool))  # True
print(isinstance(True, int))  # True, так как bool -- подкласс int
print(isinstance('a string', object))  # True, всё является объектами
print(isinstance(None, object))  # True, даже None
print(isinstance(False, str))  # False
print(isinstance(int, type))  # True, любой класс -- объект-экземпляр метакласса type
print(isinstance(42, type))  # False, 42 -- это не тип данных
