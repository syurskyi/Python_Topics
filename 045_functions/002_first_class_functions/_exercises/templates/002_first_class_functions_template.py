# -*- coding: utf-8 -*-

# functions_are_objects

# ___ my_function
#     print I am a function

# print Functions are objects_ i_ m_, o_

# print()

# ######################################################################################################################
# You can use variables to store functions
# ___ my_function
#     print I am a function
#
# test _ my_function
# test
#
# # print()
# ######################################################################################################################
# You can pass functions as parameters

# ___ call_passed_function incoming
#     print Calling!
#     ?()
#     print Called!

# call_passed_function my_function

# print()
# ######################################################################################################################
# You can check if something could be called

# print(c_(le_ , c_ 45, c_(c_

# print()
# ######################################################################################################################
# You can return function from a function

# ___ return_min_function
#     r_ min

# test = return_min_function__
# min_value = ? 4 5 -9 12
# print Min values is_  min_value

# print()

# ######################################################################################################################
# functions_as_first_class_objects

# Создание ссылки на объект
# out = print
# out Hello

# Сохранение ссылок на функции в структуре данных

# ___ add x y
#     r_ x + y
#
# ___ sub x y
#     r_ x - y
#
# operations _ _
#     _+_| a_
#     _-_| s_
# _

# print(o_|_+_||2_ 3||
# print(o_|_-_||2_ 3||

# print()

# ######################################################################################################################
# Functions and Methods are callable

# print ca_ print
# print ca_ l_
# l = [1, 2, 3]
# print ca_ l.a_
# s = 'abc'
# print ca_ s.u_
#
# print()
# ######################################################################################################################
# Callables always return a value:

# result _ print hello
# print ?
#
# l = [1, 2, 3]
# result _ ?.a_ 4
# print ?
# print ?
#
# s _ abc
# result _ ?.u_
# print ?
#
# print()
# ######################################################################################################################
# Classes are callable:

# f_ d_ i_ D_
# ca_ D_
# result _ D_ 10.5
# print ?
#
# print()
# # ######################################################################################################################
# Class instances may be callable:

# c_ MyClass
#     ___ __i_ ___
#         print initializing...'
#         _.counter = 0
#
#     ___ -c s_ x_1
#         _.counter += x
#         print s_.counter
#
# my_obj _ MyClass
# ca_ my_obj. -i
# ca_(my_obj. -c
# my_obj
# my_obj
# my_obj(10)
#
# print()

# ######################################################################################################################
# # Пример работы с функциями как с объектами первого класса
# """Пример работы с функциями как с объектами первого класса"""
#
# # Создание ссылки на объект
# out = print
# out('Hello')
#
# # Сохранение ссылок на функции в структуре данных
#
# ___ add x y
#     r_ x + y
#
# ___ sub x y
#     r_ x - y
#
# operations = {
#     '+': add,
#     '-': sub
# }
#
# print(?['+'](2, 3))
# print(?['-'](2, 3))
#
# print()

# ######################################################################################################################
# Python program to illustrate functions
# can be treated as objects


# ___ shout text
#     r_ ? *u____
#
#
# print shout__Hello__
#
# yell _ shout
#
# print yell__Hello___


# Python program to illustrate functions
# can be passed as arguments to other functions
# ___ shout text
#     r_ t_*u_


# ___ whisper text
#     r_ t_*l____
#
#
# ___ greet func
#     # storing the function in a variable
#     greeting - func _Hi, I am created by a function passed as an argument._
#     print greeting
#
#
# greet _shout_
# greet _whisper_


# Python program to illustrate functions
# Functions can return another function

# ___ create_adder x
#     __ adder y
#         r_ x + y
#
#     r_ ad___
#
#
# add_15 _ cr_ad 15
#
# print add_15_10__


