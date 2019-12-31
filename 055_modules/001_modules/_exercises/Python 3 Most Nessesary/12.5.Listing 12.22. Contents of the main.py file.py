# # -*- coding: utf-8 -*-
#
# # Доступ к модулю folder1\module1.py
# _____ folder1.module1 __ m1
#                          # Выведет: __init__ из folder1
# print ?.m..            # Выведет: Модуль folder1.module1
# from folder1 _____ mo_1 __ m2
# print ?.m..            # Выведет: Модуль folder1.module1
# from folder1.module1 _____ msg
# print ?               # Выведет: Модуль folder1.module1
#
# # Доступ к модулю folder1\folder2\module2.py
# _____ f1.f2.mo_2 __ m3
#                          # Выведет: __init__ из folder1.folder2
# print ?.m..            # Выведет: Модуль folder1.folder2.module2
# from folder1.folder2 _____ module2 __ m4
# print ?.m..            # Выведет: Модуль folder1.folder2.module2
# from folder1.folder2.module2 _____ msg
# print ?               # Выведет: Модуль folder1.folder2.module2
#
# input()
#
#
# _____ f1.f2.mo_2
#
#
# print(f1.f2.mo_2.m..
#
#
# _____ f1.f2.mo_2 __ m
# print ?.m..
#
#
# _____ f1.f2 _____ module2
# print(mo_2.m..
#
#
# ______ f1.f2.mo_2 _____ msg
# print ?
#
# ____ f1.f2.mo_2 _____ *
# print(msg)
#
#
# # -*- coding: utf-8 -*-
# -a _  module2", "module3
