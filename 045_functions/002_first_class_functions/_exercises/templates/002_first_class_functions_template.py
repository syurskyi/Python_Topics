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
# test  my_function
# test
#
# # print()
# ######################################################################################################################
# You can pass functions as parameters

# ___ call_passed_function incoming
#     print Calling!
#     i_()
#     print Called!

# call_passed_function my_function

# print()
# ######################################################################################################################
# You can check if something could be called

# print(c_(l_), c_ 45 c_(c_))

# print()
# ######################################################################################################################
# You can return function from a function

# ___ return_min_function
#     r_ min

# test = return_min_function__
# min_value = t_  4 5 -9 12
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

# ca_ print
# ca_ l_
# l = [1, 2, 3]
# ca_ l.a_
# s = 'abc'
# ca_ s.u_
#
# print()
# ######################################################################################################################
# Callables always return a value:

# result _ print hello
# print result
#
# l = [1, 2, 3]
# result _ l.a_ 4
# print result
# print l
#
# s _ abc
# result _ s.u_
# print result
#
# print()
# ######################################################################################################################
# Classes are callable:

# f_ d_ i_ D_
# ca_ D_
# result _ D_ 10.5
# print result
#
# print()
# # ######################################################################################################################
# Class instances may be callable:

# c_ MyClass
#     ___ __i_ ___
#         print initializing...'
#         _.counter = 0
#
#     ___ __c_(s_ x_1
#         _.counter += x
#         print s_.counter
#
# my_obj _ MyClass
# ca_ my_obj.__i_
# ca_(my_obj.__c_
# my_obj()
# my_obj()
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
# print(oper___['+'](2, 3))
# print(oper___['-'](2, 3))
#
# print()