# # -*- coding: utf-8 -*-
#
# ______ j..
# from ty.. ______ D..
#
#
# c_ Flyweight
#     """
#     Легковес хранит общую часть состояния (также называемую внутренним
#     состоянием), которая принадлежит нескольким реальным бизнес-объектам.
#     Легковес принимает оставшуюся часть состояния (внешнее состояние, уникальное
#     для каждого объекта) через его параметры метода.
#     """
#
#     ___ - shared_state ? __ ?
#         _?  ?
#
#     ___ operation unique_state ? __ ?
#         s = j___.d.. _s..
#         u = j___.d.. ?
#         print _*Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")
#
#
# c_ FlyweightFactory
#     """
#     Фабрика Легковесов создает объекты-Легковесы и управляет ими. Она
#     обеспечивает правильное разделение легковесов. Когда клиент запрашивает
#     легковес, фабрика либо возвращает существующий экземпляр, либо создает
#     новый, если он ещё не существует.
#     """
#
#     _flyweights Di.. |st. Fl.. _     # dict
#
#     ___ -  initial_flyweights D.. __ ?
#         ___ state __ ?
#             _fl..|g_k.. ? _ F.. ?
#
#     ___ get_key state D.. __ ?
#         """
#         Возвращает хеш строки Легковеса для данного состояния.
#         """
#
#         r_ "_".jo.. so.. ?
#
#     ___ get_flyweight shared_state D.. __ F..
#         """
#         Возвращает существующий Легковес с заданным состоянием или создает
#         новый.
#         """
#
#         key = g_k. ?
#
#         __ no _f__.ge. ?
#             print("FlyweightFactory: Can't find a flyweight, creating new one.")
#             _f...|? _ F.. ?
#         ____
#             print("FlyweightFactory: Reusing existing flyweight.")
#
#         r_ _f___|?
#
#     ___ list_flyweights __ ?
#         count = le. _f..
#         print _*FlyweightFactory: I have |? flyweights:")
#         print("\n".jo.. ma. st. _f__.ke. en._""
#
#
# ___ add_car_to_police_database(
#     factory: FF.. plates: ?, owner: ?,
#     brand: ?, model: ?, color: ?
# ) __ ?
#     print("\n\nClient: Adding a car to database.")
#     flyweight = f____.g_f.. b.. m.. c..
#     # Клиентский код либо сохраняет, либо вычисляет внешнее состояние и передает
#     # его методам легковеса.
#     f___.o.. p.. o..
#
#
# __ _______ __ ______
#     """
#     Клиентский код обычно создает кучу предварительно заполненных легковесов на
#     этапе инициализации приложения.
#     """
#
#     factory = FF...||
#         |"Chevrolet", "Camaro2018", "pink"|
#         |"Mercedes Benz", "C300", "black"|
#         |"Mercedes Benz", "C500", "red"|
#         |"BMW", "M5", "red"|
#         |"BMW", "X6", "white"|
#     ||
#
#     ?.l_f..
#
#     add_car_to_police_database|
#         ? "CL234IR", "James Doe", "BMW", "M5", "red")
#
#     add_car_to_police_database|
#         ? "CL234IR", "James Doe", "BMW", "X1", "red")
#
#     print("\n")
#
#     ?.l_f..
#
# # FlyweightFactory: I have 5 flyweights:
# # Camaro2018_Chevrolet_pink
# # C300_Mercedes Benz_black
# # C500_Mercedes Benz_red
# # BMW_M5_red
# # BMW_X6_white
# #
# # Client: Adding a car to database.
# # FlyweightFactory: Reusing existing flyweight.
# # Flyweight: Displaying shared (["BMW", "M5", "red"]) and unique (["CL234IR", "James Doe"]) state.
# #
# # Client: Adding a car to database.
# # FlyweightFactory: Can't find a flyweight, creating new one.
# # Flyweight: Displaying shared (["BMW", "X1", "red"]) and unique (["CL234IR", "James Doe"]) state.
# #
# # FlyweightFactory: I have 6 flyweights:
# # Camaro2018_Chevrolet_pink
# # C300_Mercedes Benz_black
# # C500_Mercedes Benz_red
# # BMW_M5_red
# # BMW_X6_white
# # BMW_X
# 1_red