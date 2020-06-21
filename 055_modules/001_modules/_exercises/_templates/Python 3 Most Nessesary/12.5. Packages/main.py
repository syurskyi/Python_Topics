# # -*- coding: utf-8 -*-
#
# # Доступ к модулю folder1\module1.py
# _____ f_1.m_1 __ m1
#                          # Выведет: __init__ из folder1
# print(_1.msg)            # Выведет: Модуль folder1.module1
# from folder1 _____ m_1 __ m2
# print(_2.m..            # Выведет: Модуль folder1.module1
# from folder1.module1 _____ msg
# print ?               # Выведет: Модуль folder1.module1
#
# # Доступ к модулю folder1\folder2\module2.py
# _____ folder1.folder2.module2 __ m3
#                          # Выведет: __init__ из folder1.folder2
# print(_3.m..            # Выведет: Модуль folder1.folder2.module2
# ____ f_1.f_2 _____ m_2 __ m4
# print(_4.m..            # Выведет: Модуль folder1.folder2.module2
# ____ f_1.f_2.m_2 _____ msg
# print ?               # Выведет: Модуль folder1.folder2.module2
#
# input()
#
#
# _____ f_1.f_2.m_2
#
#
# print(f_1.f_2.m_2.m..
#
#
# _____ f_1.f_2.m_2 __ m
# print ?.m..
#
#
# from f_1.f_2 _____ m_2
# print ?.m..
#
#
# from f_1.f_2.m_2 _____ msg
# print ?
#
#
# from f_1.f_2.m_2 _____ *
# print ?
#
#
# # -*- coding: utf-8 -*-
# -a _ m_2 module3
