# # -*- coding: utf-8 -*-
#
# ____ -f ______ a..
# ____ a.. ______ ABC, a..
#
#
# c_ Command A..
#     """
#     Интерфейс Команды объявляет метод для выполнения команд.
#     """
#
#     ??
#     ___ execute __ ?
#         p..
#
#
# c_ SimpleCommand C..
#     """
#     Некоторые команды способны выполнять простые операции самостоятельно.
#     """
#
#     ___ - payload st. __ ?
#         _payload _ payload
#
#     ___ execute __ ?
#         print(_*SimpleCommand: See, I can do simple things like printing"
#               _*||_p..
#
#
# c_ ComplexCommand C..
#     """
#     Но есть и команды, которые делегируют более сложные операции другим
#     объектам, называемым «получателями».
#     """
#
#     ___ - receiver R.. a st. b st. __ ?
#         """
#         Сложные команды могут принимать один или несколько объектов-получателей
#         вместе с любыми данными о контексте через конструктор.
#         """
#
#         _?  ?
#         _?  ?
#         _?  ?
#
#     ___ execute __ ?
#         """
#         Команды могут делегировать выполнение любым методам получателя.
#         """
#
#         print("ComplexCommand: Complex stuff should be done by a receiver object", e.._"")
#         -r__.d_s.. _a
#         -r__.d_s_e.. _b
#
#
# c_ Receiver
#     """
#     Классы Получателей содержат некую важную бизнес-логику. Они умеют выполнять
#     все виды операций, связанных с выполнением запроса. Фактически, любой класс
#     может выступать Получателем.
#     """
#
#     ___ do_something a st. __ ?
#         print(_*\nReceiver: Working on ||?.)", e.._"")
#
#     ___ do_something_else b st. __ ?
#         print(_*\nReceiver: Also working on ||?.)", e.._"")
#
#
# c_ Invoker
#     """
#     Отправитель связан с одной или несколькими командами. Он отправляет запрос
#     команде.
#     """
#
#     _on_start _ N..
#     _on_finish _ N..
#
#     """
#     Инициализация команд.
#     """
#
#     ___ set_on_start command C..
#         _on_start _ ?
#
#     ___ set_on_finish command C..
#         _on_finish _ ?
#
#     ___ do_something_important __ ?
#         """
#         Отправитель не зависит от классов конкретных команд и получателей.
#         Отправитель передаёт запрос получателю косвенно, выполняя команду.
#         """
#
#         print("Invoker: Does anybody want something done before I begin?")
#         __ isi.. _o_s_ C..
#             _o_s__.ex..
#
#         print("Invoker: ...doing something really important...")
#
#         print("Invoker: Does anybody want something done after I finish?")
#         __ isi.. _o_f.. C..
#             _o_f__.e..
#
#
# __ _______ __ ______
#     """
#     Клиентский код может параметризовать отправителя любыми командами.
#     """
#
#     invoker _ I..
#     ?.s_o_s.. S.. "Say Hi!"
#     receiver _ R..
#     i___.s_o_f.. CC..(
#         r... "Send email", "Save report"
#
#     i____.d_s_i..
#
# # Invoker: Does anybody want something done before I begin?
# # SimpleCommand: See, I can do simple things like printing (Say Hi!)
# # Invoker: ...doing something really important...
# # Invoker: Does anybody want something done after I finish?
# # ComplexCommand: Complex stuff should be done by a receiver object
# # Receiver: Working on (Send email.)
# # Receiver: Also working on (Save report.)
