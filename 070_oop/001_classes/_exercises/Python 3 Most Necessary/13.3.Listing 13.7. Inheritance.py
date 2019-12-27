# # -*- coding: utf-8 -*-

# c_ Class1         # Базовый класс
#     ___ func1 ____
#         print("Метод func1() класса Class1")
#     ___ func2 ____
#         print("Метод func2() класса Class1")
#
# c_ Class2 C..  # Класс Class2 наследует класс Class1
#     ___ func3 ____
#         print("Метод func3() класса Class2")
# c _ C2        # Создаем экземпляр класса Class2
# ?.f_1            # Выведет: Метод func1() класса Class1
# ?.f_2           # Выведет: Метод func2() класса Class1
# ?.f_3          # Выведет: Метод func3() класса Class2