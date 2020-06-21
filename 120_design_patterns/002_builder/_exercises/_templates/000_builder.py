# # -*- coding : utf-8 -*-
# #

# # abc.ABC basically just an extra layer over metaclass_abc.ABCMeta. i.e abc.ABC implicitly defines the metaclass for us.
# # The only difference is that in the former case you need a simple inheritance and in the latter you need
# # to specify the metaclass.
# # New class ABC has ABCMeta as its meta class. Using ABC as a base class has essentially the same effect as specifying
# # metaclass_abc.ABCMeta, but is simpler to type and easier to read.

# #
# # class abc.ABC
# #    A helper class that has ABCMeta as its metaclass. With this class, an abstract base class can be created by
# #    simply deriving from ABC avoiding sometimes confusing metaclass usage, for example:
# #    from abc import ABC
# #
# #   class MyABC(ABC):
# #        pass
# #    Note that the type of ABC is still ABCMeta, therefore inheriting from ABC requires the usual precautions
# #    regarding metaclass usage, as multiple inheritance may lead to metaclass conflicts. One may also define
# #    an abstract base class by passing the metaclass keyword and using ABCMeta directly, for example:
# #
# #    from abc import ABCMeta
# #
# #   class MyABC(metaclass_ABCMeta):
# #       pass
# #
# #    New in version 3.4.
# #
# #class abc.ABCMeta
# #
# #    Metaclass for defining Abstract Base Classes (ABCs).
# #    Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class.
# #    You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs
# #    as “virtual subclasses” – these and their descendants will be considered subclasses of the registering ABC
# #    by the built-in issubclass() function, but the registering ABC won’t show up in their
# #    MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable
# #    (not even via super()). 1

# ____ -f ______ an...
# ____ a.. ______ A.. a..m.. a..p..
# ____ ty.. ______ A..
#
#
# c_ Builder A..
#     """
#     Интерфейс Строителя объявляет создающие методы для различных частей объектов
#     Продуктов.
#     """
#
#     ?a_p_
#     ___ product __ N..
#         p..
#
#     ?a_m_
#     ___ produce_part_a __ N..
#         p..
#
#     ?a_m_
#     ___ produce_part_b __ N..
#         p..
#
#     ?a_m_
#     ___ produce_part_c __ N..
#         p..
#
#
# c_ ConcreteBuilder1 B..
#     """
#     Классы Конкретного Строителя следуют интерфейсу Строителя и предоставляют
#     конкретные реализации шагов построения. Ваша программа может иметь несколько
#     вариантов Строителей, реализованных по-разному.
#     """
#
#     ___ - __ N..
#         """
#         Новый экземпляр строителя должен содержать пустой объект продукта,
#         который используется в дальнейшей сборке.
#         """
#         ?re..
#
#     ___ reset __ N..
#         _product _ P_1
#
#     ?p..
#     ___ product __ P_1
#         """
#         Конкретные Строители должны предоставить свои собственные методы
#         получения результатов. Это связано с тем, что различные типы строителей
#         могут создавать совершенно разные продукты с разными интерфейсами.
#         Поэтому такие методы не могут быть объявлены в базовом интерфейсе
#         Строителя (по крайней мере, в статически типизированном языке
#         программирования).
#
#         Как правило, после возвращения конечного результата клиенту, экземпляр
#         строителя должен быть готов к началу производства следующего продукта.
#         Поэтому обычной практикой является вызов метода сброса в конце тела
#         метода getProduct. Однако такое поведение не является обязательным, вы
#         можете заставить своих строителей ждать явного запроса на сброс из кода
#         клиента, прежде чем избавиться от предыдущего результата.
#         """
#         product _ _product
#         ?re..
#         r_ ?
#
#     ___ produce_part_a __ N..
#         ._pr__.ad.. "PartA1"
#
#     ___ produce_part_b __ N..
#         _pr__.ad.. "PartB1"
#
#     ___ produce_part_c __ N..
#         _pr_.ad.. "PartC1"
#
#
# c_ Product1
#     """
#     Имеет смысл использовать паттерн Строитель только тогда, когда ваши продукты
#     достаточно сложны и требуют обширной конфигурации.
#
#     В отличие от других порождающих паттернов, различные конкретные строители
#     могут производить несвязанные продукты. Другими словами, результаты
#     различных строителей могут не всегда следовать одному и тому же интерфейсу.
#     """
#
#     ___ - __ N..
#         ?parts _      # list
#
#     ___ add  part A.. __ N..
#         ?p__.ap.. ?
#
#     ___ list_parts __ N..
#         print _*Product parts: |', '.jo.. ?p.. " en._"")
#
#
# c_ Director
#     """
#     Директор отвечает только за выполнение шагов построения в определённой
#     последовательности. Это полезно при производстве продуктов в определённом
#     порядке или особой конфигурации. Строго говоря, класс Директор необязателен,
#     так как клиент может напрямую управлять строителями.
#     """
#
#     ___ - __ N..
#         _builder _ N..
#
#     ?p..
#     ___ builder __ B..
#         r__ _b..
#
#     ??.?
#     ___ builder  builder B.. __ N..
#         """
#         Директор работает с любым экземпляром строителя, который передаётся ему
#         клиентским кодом. Таким образом, клиентский код может изменить конечный
#         тип вновь собираемого продукта.
#         """
#         _?  ?
#
#     """
#     Директор может строить несколько вариаций продукта, используя одинаковые
#     шаги построения.
#     """
#
#     ___ build_minimal_viable_product __ N..
#         ?b__.p_a..
#
#     ___ build_full_featured_product __ N..
#         ?b__.p_a
#         ?b__.p_b
#         ?b__.p_c
#
#
# __ _______ __ ______
#     """
#     Клиентский код создаёт объект-строитель, передаёт его директору, а затем
#     инициирует процесс построения. Конечный результат извлекается из объекта-
#     строителя.
#     """
#
#     director _ D..
#     builder _ C..
#     d__.b.. _ b...
#
#     print("Standard basic product: ")
#     d__.b_m
#     b___.pr__.l_p..
#
#     print("\n")
#
#     print("Standard full featured product: ")
#     d__.b_f_f_p..
#     b___.p__.l_p..
#
#     print("\n")
#
#     # Помните, что паттерн Строитель можно использовать без класса Директор.
#     print("Custom product: ")
#     b___.p_a
#     b___.p_b
#     b___.p__.l_p..
