# # # # -*- coding: utf-8 -*-
# #
# # c_ Class1         # Базовый класс для класса Class2
# #     ___ func1 ____
# #         print("Метод func1() класса Class1")
# #
# # c_ Class2 _1 # Класс Class2 наследует класс Class1
# #     ___ func2 ____
# #         print("Метод func2() класса Class2")
# #
# # c_ Class3 _1 # Класс Class3 наследует класс Class1
# #     ___ func1 ____
# #         print("Метод func1() класса Class3")
# #     ___ func2 ____
# #         print("Метод func2() класса Class3")
# #     ___ func3 ____
# #         print("Метод func3() класса Class3")
# #     ___ func4 ____
# #         print("Метод func4() класса Class3")
# #
# # c_ Class4 _2 _3 # Множественное наследование
# #     ___ func4 ____
# #         print("Метод func4() класса Class4")
# # c = C_4           # Создаем экземпляр класса Class4
# # ?._1                # Выведет: Метод func1() класса Class3
# # ?._2                # Выведет: Метод func2() класса Class2
# # ?._3                # Выведет: Метод func3() класса Class3
# # ?._4                # Выведет: Метод func4() класса C_4
#
#
# c_ Class4 C..2 C..3 # Множественное наследование
#     # Наследуем func2() из класса Class3, а не из класса Class2
#     func2 _ C.3.f.2
#     _ func4 ____
#         print("Метод func4() класса Class4")
#
#
# print(C.1. -b
# print(C.2. -b
# print(C.3. -b
# print(C.4. -b