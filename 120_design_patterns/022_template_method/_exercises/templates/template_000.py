# # -*- coding: utf-8 -*-
#
# ____ a.. _______ A.. a..
#
# c_ AbstractClass A..
#     """
#     Абстрактный Класс определяет шаблонный метод, содержащий скелет некоторого
#     алгоритма, состоящего из вызовов (обычно) абстрактных примитивных операций.
#
#     Конкретные подклассы должны реализовать эти операции, но оставить сам
#     шаблонный метод без изменений.
#     """
#
#     ___ template_method __ ?
#         """
#         Шаблонный метод определяет скелет алгоритма.
#         """
#
#         b_1
#         r_1
#         b_2
#         h_1
#         r_2
#         b_3
#         h_2
#
#     # Эти операции уже имеют реализации.
#
#     ___ base_operation1 __ ?
#         print("AbstractClass says: I am doing the bulk of the work")
#
#     ___ base_operation2 __ ?
#         print("AbstractClass says: But I let subclasses override some operations")
#
#     ___ base_operation3 __ ?
#         print("AbstractClass says: But I am doing the bulk of the work anyway")
#
#     # А эти операции должны быть реализованы в подклассах.
#
#     ??
#     ___ required_operations1 __ ?
#         p..
#
#     ??
#     ___ required_operations2 __ ?
#         p..
#
#     # Это «хуки». Подклассы могут переопределять их, но это не обязательно,
#     # поскольку у хуков уже есть стандартная (но пустая) реализация. Хуки
#     # предоставляют дополнительные точки расширения в некоторых критических
#     # местах алгоритма.
#
#     ___ hook1 __ ?
#         p..
#
#     ___ hook2 __ ?
#         p..
#
#
# c_ ConcreteClass1 A..
#     """
#     Конкретные классы должны реализовать все абстрактные операции базового
#     класса. Они также могут переопределить некоторые операции с реализацией по
#     умолчанию.
#     """
#
#     ___ required_operations1 __ ?
#         print("ConcreteClass1 says: Implemented Operation1")
#
#     ___ required_operations2 __ ?
#         print("ConcreteClass1 says: Implemented Operation2")
#
#
# c_ ConcreteClass2 A..
#     """
#     Обычно конкретные классы переопределяют только часть операций базового
#     класса.
#     """
#
#     ___ required_operations1 __ ?
#         print("ConcreteClass2 says: Implemented Operation1")
#
#     ___ required_operations2 __ ?
#         print("ConcreteClass2 says: Implemented Operation2")
#
#     ___ hook1 __ ?
#         print("ConcreteClass2 says: Overridden Hook1")
#
#
# ___ client_code abstract_class A.. __ ?
#     """
#     Клиентский код вызывает шаблонный метод для выполнения алгоритма. Клиентский
#     код не должен знать конкретный класс объекта, с которым работает, при
#     условии, что он работает с объектами через интерфейс их базового класса.
#     """
#
#     # ...
#     ?.t_m..
#     # ...
#
#
# __ ________ __ _________
#     print("Same client code can work with different subclasses:")
#     ? C1
#     print("")
#
#     print("Same client code can work with different subclasses:")
#     ? C2