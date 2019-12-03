# # -*- coding: utf-8 -*-
#
# """
# Пример использования утиной типизации для работы с объектами, которые реализуют
# определённый интерфейс.
#
# В этом примере логически существует интерфейс "фигура", описываемый методом render,
# хоть он и не описан отдельным абстрактным классом.
# """
#
# # Классы из предыдущего примера
#
# c_ IsoscelesShape o..
#     ___ - ____ side
#         ____.s.. _ s..
#
#     ___ render ____
#         print(____)
#         ____.dr..
#         print()
#
#     ___ -s ____
#         r_ 'Abstract figure object'
#
#     ___ draw ____
#         p____
#
#
# c_ Square I..
#     ___ draw ____
#         ___ _ i_ ra.. ____.s..
#             print('*' * ____.s..
#
#     ___ -s ____
#         r_ 'Square with a side of |!r '.f... ____.s..
#
#
# c_ IsoscelesRightTriangle S..
#     ___ draw ____
#         ___ i i_ ra.. 1, ____.s.. + 1
#             print('*' * i)
#
#     ___ -s ____
#         r_ 'Isosceles right triangle with a side of {!r}'.f... ____.s..
#
#
# # Класс, который не наследуется от классов равнобедренных фигур
# c_ Rectangle o..
#     ___ -  ____ width, height
#         ____.w... _ w...
#         ____.h... _ h...
#
#     ___ render ____
#         print('Rectangle with sides {!r} and |!r '.f... ____.w.. ____.h..
#         print('\n'.j.. '*' 0 ____.w..| 0 ____.h..
#         print()
#
#
# ___ m..
#     shapes _ S.. 5  I.. 3 R.. 10 3
#     ___ shape i_ ?
#         s_.r..
#
# __ ______ __ _____
#     m..
