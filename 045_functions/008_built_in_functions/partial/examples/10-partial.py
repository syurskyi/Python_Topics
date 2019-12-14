"""Пример использования функции partial модуля functools"""

from functools import partial

# Частичное применение функции
print_with_comma = partial(print, sep=', ')

print_with_comma(2, 3, 5)
