# # -*- coding: utf-8 -*-
#
# ____ a.. i____ A.. a..
# c_ Class1 m..
#     ??
#     ___ func  x     # Абстрактный метод
#         p..
#
# c_ Class2 ?      # Наследуем абстрактный метод
#     ___ func  x     # Переопределяем метод
#         print ?
# c_ Class3 ?      # Класс не переопределяет метод
#     p..
#
# c2 = Class2()
# c2.func(50)                # Выведет: 50
# ___
#     c3 = _3          # Ошибка. Метод func() не переопределен
#     ?.f.. 50
# _______ T.. __ msg
#     print ?            # Can't instantiate abstract class Class3
#                            # with abstract methods func