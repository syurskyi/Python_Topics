# # -*- coding: utf-8 -*-
#
# """
# Пример использования полиморфизма
# """
#
# c_ IsoscelesShape o...
#     ___ - ____ side)
#         ____.s.. _ s..
#
#     ___ render ____
#         print ____
#         ____.draw
#         print()
#
#     ___ __str__ ____
#         r_ 'Abstract figure object'
#
#     ___ draw ____
#         p..
#
#
# c_ Square I..
#     ___ draw ____
#         ___ _ i_ ra.. ____.s..
#             print('*' * ____.s..
#
#     ___ __s ____
#         r_ 'Square with a side of |!r'.f... ____.s..
#
#
# c_ IsoscelesRightTriangle S..
#     ___ draw ____
#         ___ i i_ ra.. 1, ____.s.. + 1
#             print('*' * i)
#
#     ___ __s ____
#         r_ 'Isosceles right triangle with a side of |!r'.f... ____.s..
#
#
# ___ m..
#     shapes =  S. 5 I.. 3 S... 7 I... 8
#     ___ shape i_ ?
#         s___.r..
#
#
# __ _______ __ _____
#     m..
