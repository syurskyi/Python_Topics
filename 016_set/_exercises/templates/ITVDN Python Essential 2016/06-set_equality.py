# -*- coding: utf-8 -*-

"""Проверка множеств на равенство происходит поэлементно,
независимо от типов множеств.
"""

print({1, 2, 3} == frozenset([1, 2, 3]))
print(set('abc') == frozenset('abc'))
print(set('abc') in set([frozenset('abc')]))