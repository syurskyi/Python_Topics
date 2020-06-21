"""Пример использования функций takewhile и dropwhile модуля itertools"""

from itertools import takewhile, dropwhile


numbers = [1, 4, 6, 4, 1]
predicate = lambda x: x < 5

for value in takewhile(predicate, numbers):
    print(value)

print()

for value in dropwhile(predicate, numbers):
    print(value)
