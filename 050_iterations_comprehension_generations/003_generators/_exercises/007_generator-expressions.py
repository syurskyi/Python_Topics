# # -*- coding: utf-8 -*-
#
# # generator-expressions
#
# # Некоторые простые генераторы могут быть записаны в виде выражения.
# # Они выглядят как выражение, содержащее некоторые переменные, после
# # которого одно или несколько ключевых слов for, задающих, какие значения
# # должны принимать данные переменные  синтаксис соответствует заголовку
# #     цикла for , и ноль или несколько условий, фильтрующих генерируемые
# # значения  синтаксис соответствует заголовку оператора if . Такие выражения
# # называются выражениями-генераторами  generator expressions .
# #
# generator _  x ** 2 + y ___ x i_ ra... 2, 7  ___ y i_ ra... 3  i_ x !_ 6
# ___ number i_ g...
#     print n....
#
# print
#
# print su. 2 * x ___ x i_ ra... 5
#
# # delegating-to-subgenerator
#
# # В Python 3 существуют так называемые подгенераторы  subgenerators .
# # Если в функции-генераторе встречается пара ключевых слов yield from,
# # после которых следует объект-генератор, то данный генератор делегирует
# # доступ к подгенератору, пока он не завершится  не закончатся его значения ,
# # после чего продолжает своё исполнение.
# #
# #
# ___ generator
#     y___ f...   3 * x ___ x i_ ra... 5
#     y___ f...   2 * x ___ x i_ ra... 5, 10
#
#
# ___ i i_ generator
#     print i
