﻿# # -*- coding: utf-8 -*-
#
# """Использование представлений словарей"""
#
# # Объекты, возвращаемые методами items(), keys() и values() (viewitems(),
# # viewkeys(), viewvalues() в Python 2.7) – это объекты представления словаря.
# # Они предоставляют динамическое представление элементов словаря, то есть
# # изменения данного словаря автоматически отображаются и на этих объектах.
# #
# # Операции с представлениями словарей:
# # • iter(dictview) – получение итератора
# #   по ключам, значениям или парам ключей и значений.  Все представления словарей
# #   при итерировании возвращают элементы словаря в одинаковом порядке.  При
# #   попытке изменить словарь во время итерирования может возникнуть исключение
# #   RuntimeError.
# # • len(dictview) – количество элементов в словаре.
# # • x in dictview – проверка существования ключа, значения или пары ключ-значение
# #   в словаре.
#
# dishes _ eggs 2 sausage 1 bacon 1 spam 500
# keys _ ?.?
# values _ ?.?
#
# # Итерирование
# n = 0
# ___ val __ v..
#     n +_ ?
# print ?
#
# # Ключи и значения итерируются в таком же порядке
# print(l.. k..
# print(l.. v..
#
# # Объекты представлений динамически отображают изменения в словаре
# del dishes['eggs']
# del dishes['sausage']
# print li.. k..
#
# # Также они поддерживают операции с множествами
# print k.. _ 'eggs', 'bacon', 'salad'   # Пересечение множеств | intersection
# print k.. ^ 'sausage', 'juice'         # # Симметрическая разница | symmetric_difference