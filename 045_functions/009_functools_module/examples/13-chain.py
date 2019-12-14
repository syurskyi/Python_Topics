"""Пример использования функции chain модуля itertools"""

from itertools import chain

for i in chain(range(2), range(3)):
    print(i)
