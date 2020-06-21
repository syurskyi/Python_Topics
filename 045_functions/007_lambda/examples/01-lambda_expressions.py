# -*- coding: utf-8 -*-

"""Пример использования лямбда-выражений"""

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y
}

print(operations['+'](2, 3))
print(operations['-'](2, 3))
