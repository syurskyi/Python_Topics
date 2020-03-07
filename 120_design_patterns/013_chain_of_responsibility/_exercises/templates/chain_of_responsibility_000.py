# # -*- coding: utf-8 -*-
#
# ____ -f ______ a...
# ____ a.. ______ A.. a..
# ____ ty.. ______ A.. O..
#
#
# c_ Handler A..
#     """
#     Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
#     также объявляет метод для выполнения запроса.
#     """
#
#     ??
#     ___ set_next handler H.. __ H..
#         p..
#
#     ??
#     ___ handle request __ O..|st..
#         p..
#
#
# c_ AbstractHandler H..
#     """
#     Поведение цепочки по умолчанию может быть реализовано внутри базового класса
#     обработчика.
#     """
#
#     _next_handler H.. _ N..
#
#     ___ set_next handler H... __ H..
#         _next_handler _ ?
#         # Возврат обработчика отсюда позволит связать обработчики простым
#         # способом, вот так:
#         # monkey.set_next(squirrel).set_next(dog)
#         r_ h...
#
#     ??
#     ___ handle request A.. __ st..
#         __ _n..
#             r_ _n__.h.. ?
#
#         r_ N..
#
#
# """
# Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
# следующему обработчику в цепочке.
# """
#
#
# c_ MonkeyHandler A..
#     ___ handle request A.. __ ?
#         __ ? __ "Banana":
#             r_ _*Monkey: I'll eat the |?
#         ____
#             r_ s___ .h.. ?
#
#
# c_ SquirrelHandler A..
#     ___ handle request A.. __ ?
#         __ ? __ "Nut":
#             r_ _*Squirrel: I'll eat the |?
#         ____
#             r_ s___ .h.. ?
#
#
# c_ DogHandler A..
#     ___ handle request A.. __ ?
#         __ ? __ "MeatBall":
#             r_ _*Dog: I'll eat the |?
#         ____
#             r_ s___ .h.. ?
#
#
# ___ client_code handler H.. __ N..
#     """
#     Обычно клиентский код приспособлен для работы с единственным обработчиком. В
#     большинстве случаев клиенту даже неизвестно, что этот обработчик является
#     частью цепочки.
#     """
#
#     ___ food __ "Nut", "Banana", "Cup of coffee"   # list
#         print(_*\nClient: Who wants a |? ?
#         result _ h__.h.. ?
#         __ ?
#             print(_*  |? ", e.._"")
#         ____
#             print(_*  |f.. was left untouched.", e.._"")
#
#
# __ _______ __ ______
#     monkey _ M..
#     squirrel _ S..
#     dog _ D..
#
#     m___.s_n.. sq___.se_n. d..
#
#     # Клиент должен иметь возможность отправлять запрос любому обработчику, а не
#     # только первому в цепочке.
#     print("Chain: Monkey > Squirrel > Dog")
#     c.. m..
#     print("\n")
#
#     print("Subchain: Squirrel > Dog")
#     c.. sq..
#
# # Chain: Monkey > Squirrel > Dog
# #
# # Client: Who wants a Nut?
# #   Squirrel: I'll eat the Nut
# # Client: Who wants a Banana?
# #   Monkey: I'll eat the Banana
# # Client: Who wants a Cup of coffee?
# #   Cup of coffee was left untouched.
# #
# # Subchain: Squirrel > Dog
# #
# # Client: Who wants a Nut?
# #   Squirrel: I'll eat the Nut
# # Client: Who wants a Banana?
# #   Banana was left untouched.
# # Client: Who wants a Cup of coffee?
# #   Cup of coffee was left untouched.