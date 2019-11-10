# # Реализация с помощью именованных функций:
# ___ make_adder x
#     ___ adder n
#         r_ x + n # захват переменной "x" из внешнего контекста
#     r_ ad____
#
# # То же самое, но через безымянные функции:
# make_adder _ l_ x| _lambda n: x + n)
#
# f _ make_adder 10
# print f|5|| # 15
# print f|-1|| # 9
#
#
# ___ multiplier n  # multiplier возвращает функцию умножения на n
#     def mul(k):
#         r_ n * k
#     r_ mul
#
#
# mul3 _ multiplier 3   # mul3 - функция, умножающая на 3
# print mul3|3|_ mul3|5||
#
# n = 3
#
# ___ mult k mul_n
#     r_ mul * k
#
#
# n = 7
# print mult 3
# n = 13
# print mult 5
#
# n = 10
# mult = l_ k_ mul_n| mul * k
# print mult 3
#
#
# ___ outer_func(x
#     ___ inner_func y
#         # inner_func замкнуло в себе х
#         r_ y + x
#     r_ in__f__