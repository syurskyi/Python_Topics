"""Пример использования комбинаторных генераторов модуля itertools"""

from itertools import permutations, combinations, combinations_with_replacement

print(list(permutations('ABC', 2)))
print()

print(list(combinations('ABC', 2)))
print()

print(list(combinations_with_replacement('ABC', 2)))
