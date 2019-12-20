# -*- coding: utf-8 -*-

"""Использование конструкторов"""

# Пустое множество
empty_set = set()
print(empty_set)

# Пустое неизменяемое множество
empty_frozenset = frozenset()
print(empty_frozenset)

# Создание множеств из итерабельых объектов

my_frozenset = frozenset([4, 1, 3, 8])
my_set = set(my_frozenset)
print(my_set)
print(my_frozenset)

def get_ints(n):
    for i in range(n):
        yield i
        yield i + 1

print(list(get_ints(10)))  # все числа, возвращаемые генератором
print(set(get_ints(10)))   # множество содержит лишь уникальные значения