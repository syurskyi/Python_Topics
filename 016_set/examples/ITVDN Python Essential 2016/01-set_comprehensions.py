# -*- coding: utf-8 -*-

"""Пример создания множеств при помощи включений множеств
(аналогично списковым включениям).
Эти объекты также имеют тип set
"""

number_set = {i + j for i in range(10) for j in range(5)}
print(number_set)

char_set = {x for x in 'abracadabra' if x not in 'abc'}
print(char_set)