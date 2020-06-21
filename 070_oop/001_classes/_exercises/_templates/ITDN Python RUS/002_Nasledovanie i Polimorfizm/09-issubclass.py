# # -*- coding: utf-8 -*-
#
# """
# issubclass(cls, base) проверяет, является ли класс cls наследником класса base.
# """
#
# print iss... bo.. in.  # True
# print iss... fl.. in.  # False
# print iss... in. fl..  # False
# print iss... comp.... ty..  # False
# print iss... comp.... obj..  # True, всё наследуется от object
#
# c_ Base o..
#     p____
#
# c_ Child o...
#     p____
#
# print iss... C.. B.. # True
# print iss... B.. o...  # True
# print iss... C.. o...  # True по транзитивности
