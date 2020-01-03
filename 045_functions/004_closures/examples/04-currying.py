# -*- coding: utf-8 -*-

"""Пример каррирования функции"""

def ordinary_add(x, y):
    """Обычная функция"""
    return x + y

def curryied_add(x):
    """Каррированная функция"""

    def do_add(y):
        return x + y

    return do_add

print(ordinary_add(2, 3))
print(curryied_add(2)(3))

# Каррирование делает лёгким частичное применение функций
add_to_five = curryied_add(5)
print(add_to_five(2))
print(add_to_five(3))

print()

# В виде лямбда-выражений
ordinary_add = lambda x, y: x + y
curryied_add = lambda x: lambda y: x + y

print(ordinary_add(2, 3))
print(curryied_add(2)(3))
add_to_five = curryied_add(5)
print(add_to_five(2))
print(add_to_five(3))
