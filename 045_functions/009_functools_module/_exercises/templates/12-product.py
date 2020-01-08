"""Пример использования функции product модуля itertools"""

from itertools import product

for a, b in product(range(2), range(3)):
    print(a, b)
