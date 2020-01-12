# # -*- coding: utf-8 -*-
#
# # Generators and function application
# # Normal positionals
# #  Unpack range values: iterable in 3.X
# #  Unpack generator expression values
#
# ___ f a, b, c : print '/, /, and /' /  a, b, c
#
# f 0, 1, 2   # Normal positionals
#
# f *ra.. 3   # Unpack range values: iterable in 3.X
#
# f * i ___ i i_ ra.. 3
#
# # Generators and function application
# # dict
# # Normal keywords
# # Unpack dict: key_value
# # Unpack keys iterator
# # Unpack view iterator: iterable in 3.X
#
# D _ dict a_'Bob', b_'dev', c_40.5
#
# print D
#
# f a_'Bob', b_'dev', c_40.5   # Normal keywords
#
# f **D   # Unpack dict: key_value
#
# f *D   # Unpack keys iterator
#
# f *D.values
#
# # Generators and function application
# # ___ x in 'spam':
#
# ___ x i_ 'spam': print x.up..   e.._' '
# print
#
# li.. print x.up..  , e.._' '  ___ x i_ 'spam'
# print
#
# print * x.up..   ___ x i_ 'spam'
#
# # range-generator
# ___ my_range first second_None step_1
#     """Функция-генератор, работающая подобно стандартному классу range"""
#
#     i_ second i_ N..
#         current _ 0
#         e.. _ first
#     e____
#         current _ fi..
#         e.. _ se..
#
#     i_ step __ 0:
#         r.... V...E... 'step must not be zero'
#
#     w____  step > 0 an. cur.. < e..  o.  step < 0 an. cur... > e.. :
#         # yield выдаёт текущее значение и приостанавливает работу генератора.
#         # При следующем вызове next выполнение продолжится с этого места.
#         y____ cur...
#         cur... +_ step
#
#
# # fibonacci-sequence
# ___ fibonacci max_count :
#     """Генерация max_count чисел Фибоначчи"""
#     count _ 0
#     first second _ 0, 1
#
#     w____ count < max_count:
#         c... +_ 1
#         y____ second
#         first, second _ second, first + second
#
#
# ___ main
#     # Вывод 15 первых чисел Фибоначчи
#     ___ number i_ fibonacci 15
#         print n...
#
#
# i_ __.... ____ .....
#     ....
