# -*- coding: utf-8 -*-

# # Реализация с помощью именованных функций:
# ___ make_adder x
#     ___ adder n
#         r_ x + n # захват переменной "x" из внешнего контекста
#     r_ ?
#
# # То же самое, но через безымянные функции:
# make_adder _ l_ x |l... n x + ?)
#
# f _ ? 10
# print ? 5 # 15
# print ? -1  # 9
#print()
#
# ___ multiplier n  # multiplier возвращает функцию умножения на n
#     ___ mul k
#         r_ n * k
#     r_ ?
#
#
# mul3 _ ? 3   # mul3 - функция, умножающая на 3
# print ? 3  ? 5
#
# n _ 3
#
# ___ mult k mul_n
#     r_ m.. * k
#
#
# n = 7
# print m.. 3
# n = 13
# print m.. 5
#
# n = 10
# mult = l____ k mul_n m.. * k
# print ? 3
#
#
# ___ outer_func x
#     ___ inner_func y
#         # inner_func замкнуло в себе х
#         r_ y + x
#     r_ ?
