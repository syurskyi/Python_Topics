# # -*- coding: utf-8 -*-
#
# # В этом примере показано использование специального метода
# # __new__ для реализации такого шаблона проектирования как
# # Одиночка (Singleton).
# #
# # Одиночка — порождающий шаблон проектирования, гарантирующий,
# # что данный класс имеет только один экземпляр.
#
#
# c_ Singleton
#     _instance _ N..  # атрибут, хранящий экземпляр класса
#
#     ___ __n ___ $ $$
#         """
#         Метод __new__ вызывается при создании экземпляра класса.
#         """
#
#         # Если экземпляр ещё не создан, то создаём его
#         __ ___._i.. i. N..
#             ___._i.. _ object.__n ___ $ $$
#
#         # Возвращаем существующий экземпляр
#         r_ ___._i..
#
#     ___ -
#         ____.value _ 8
#
#
# obj1 _ ?
# print ?.v..
#
# obj2 = ?
# ?.v.. _ 42
# print _1.v..