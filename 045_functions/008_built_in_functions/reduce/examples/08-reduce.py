"""Пример использования функции reduce"""

from functools import reduce

numbers = [3, 2, 1, 8, -3, -2]
# Произведение всех чисел списка
product = reduce(lambda x, y: x * y, numbers)

print(product)
