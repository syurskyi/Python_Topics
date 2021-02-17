# -*- coding: utf-8 -*-

#  An example of using anonymous functions

# f1 = l_: 10 + 20                # Функция без параметров
# f2 = l_ x_ y_ x + y             # Функция с двумя параметрами
# f3 = l_ x y z_ x + y + z      # Функция с тремя параметрами
# print(f1())                         # Выведет: 30
# print(f2(5, 10))                    # Выведет: 15
# print(f3(5, 10, 30))                # Выведет: 45
# print()
# ######################################################################################################################
# Optional parameters in anonymous functions

# f = l_ x y=2_ x + y
# print(f(5))                         # Выведет: 7
# print(f(5, 6))                      # Выведет: 11
#
# print()

# ######################################################################################################################
# Lambda Expressions

# l_ x| x**2
#
# print()
# ######################################################################################################################
# Lambda Assigning to a Variable

# func _ l_ x| x**2
#
# type func
# func 3
#
# print()
# ######################################################################################################################
# We can specify arguments for lambdas just like we would for any function created using def, except for annotations:

# func_1 _ l_ x y_10| (x y)
# func_1 1 2
# func_1 1
#
# print()
# ######################################################################################################################
# Lambda We can even use * and **:

# func_2 _ l_ x _args y __kwargs| (x _args y {__kwargs})
#
# func_2 1 'a' 'b' y_100 a_10 b_20
#
# print()
# ######################################################################################################################
# Lambda
# Passing as an Argument
# Lambdas are functions, and can therefore be passed to any other function as an argument
# (or returned from another function)

# ___ apply_func x fn
#     r_ fn x
# apply_func 3 l_ x| x**2
# apply_func 3 l_ x| x**3
#
# print()
# ######################################################################################################################
# Lambda
# Passing as an Argument
# Lambdas are functions, and can therefore be passed to any other function as an argument
# (or returned from another function)
# we can make this even more generic:

# ___ apply_func fn _args __kwargs
#     r_ fn _args __kwargs
#
# apply_func l_ x y| x+y 1 2
# apply_func l_ x _ y| x+y 1 y_2
# apply_func l_ _args| s_ args 1 2 3 4 5
#
# print()
# ######################################################################################################################
# Lambdas and Sorting

# l = ['a', 'B', 'c', 'D']
# s_ l
# s_ l key_s_.u_
#
# # We could have used a lambda here (but you should not, this is just to illustrate using a lambda in this case):
#
# s_ l  key _ l_ s| s.u_
#
# print()
# ######################################################################################################################
# Lambdas and Sorting
# Let's look at how we might create a sorted list from a dictionary:

# d = {'def': 300, 'abc': 200, 'ghi': 100}
# d
# s_ d
#
# s_ d key_l_ k| d|k|
#
# print()

# ######################################################################################################################
# Пример использования лямбда-выражений
#
# operations = {
#     '+': l_ x, y: x + y,
#     '-': l_ x, y: x - y
# }
#
# print(oper___['+'](2, 3))
# print(oper___['-'](2, 3))
#
# print()
