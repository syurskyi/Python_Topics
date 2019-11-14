# -*- coding: utf-8 -*-

# ######################################################################################################################
# closures

# ﻿"""Пример замыкания"""
#
# ___ make_closure
#     variable _ 42
#
#     ___ closure
#         r_ v.....
#
#     r_ c....
#
# fn _ m.....
# print fn
#
# print()
# ######################################################################################################################
# advanced_closure_example

# """Демонстрация часто допускаемой ошибки и способа её решения"""

# ___ make_powers n
#     """Функция, возвращающая список функций, каждая из которых вычисляет
#     степень аргумента, равную данному индексу плюс 1
#     (неправильная реализация)
#     """

#     functions = ||
#
#     ___ i __ r_ 1 n + 1
#         f_.a_ |l_ x_ x ** i
#
#     r_ f...
#
# ___ function __ make_powers 3
#     print fu.. 2

# Видно, что результататом было не 2, 4, 8, как можно было бы ожидать,
# а 8, 8, 8

# print()

# Причиной этого является так называемое позднее связываение.  К тому моменту,
# когда вызываются функции из списка, цикл в функции make_powers уже выполнен и
# переменная i всегда равна n + 1.

# Для того, чтобы избавиться от этого, необходимо скопировать данную переменную
# в локальные переменные каждой функции.  Единственный способ создать локальную
# переменную в лямбда-выражении -- это создать параметр функции.

# ___ make_powers n
#     """Функция, возвращающая список функций, каждая из которых вычисляет
#     степень аргумента, равную данному индексу плюс 1"""

# print()
# ######################################################################################################################
# Пример каррирования функции

# ___def ordinary_add x y
#     """Обычная функция"""
#     r_ x + y
#
# ___ curryied_add x
#     """Каррированная функция"""
#
#     ___ do_add y
#         r_ x + y
#
#     r_ d....
#
# print o_(2, 3)
# print c_(2)(3)
#
# # Каррирование делает лёгким частичное применение функций
# add_to_five = c_ 5
# print a_(2)
# print a_(3)
#
# print()
#
# # В виде лямбда-выражений
# ordinary_add _ l_ x_ y_ x + y
# curryied_add _ l_ x_ l_ y_ x + y
#
# print o_(2, 3)
# print curryied_add(2)(3))
# add_to_five _ curryied_add 5
# print add_to_five(2)
# print add_to_five(3)
#
# print()

# ######################################################################################################################
# Multiple Instances of Closures
# Recall that every time a function is called, a new local scope is created.

# f_ t_ i_ p_c_
#
# ___ func
#     x _ p_c_
#     print x id x
#
# func()
# func()
#
# print()
# ######################################################################################################################
# Multiple Instances of Closures
# The same thing happens with closures, they have their own extended scope every time the closure is created:

# ___ pow n
#     # n is local to pow
#     ___ inner x
#         # x is local to inner
#         r_ x ** n
#     r_ i...

# In this example, n, in the function inner is a free variable, so we have a closure that contains inner and the free variable n

# square _ pow 2
# square 5
# cube _ pow 3
# cube 5

# We can see that the cell used for the free variable in both cases is different:

# square.__c_
# cube.__c_
#
# print()
# ######################################################################################################################
# we wrote a simple closure to count how many times a function had been run:

# ___ counter fn
#     count _ 0
#
#     ___ inner _a... __k....
#         no___
#         co__
#         co__ += 1
#         print('Function |0| was called |1| times'.f_ fn.__n_ count
#         r_ fn _a... __k...
#
#     r_ i...
#
# ___ add a b_0
#     """
#     returns the sum of a and b
#     """
#     r_ a + b
#
# add _ counter add
# add 1 2
# add 2 2
#
# print()

# ######################################################################################################################
# Пример замыкания

# ___ make_closure
#     variable _ 42
#
#     ___ closure
#         r_ var__
#
#     r_ clo___
#
# fn _ ma___cl__
# print fn
#
# print()