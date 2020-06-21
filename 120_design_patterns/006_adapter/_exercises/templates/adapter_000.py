# # -*- coding: utf-8 -*-
#
# c_ Target
#     """
#     Целевой класс объявляет интерфейс, с которым может работать клиентский код.
#     """
#
#     ___ request __ ?
#         r_ "Target: The default target's behavior."
#
#
# c_ Adaptee
#     """
#     Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
#     несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
#     некоторой доработке, прежде чем клиентский код сможет его использовать.
#     """
#
#     ___ specific_request __ ?
#         r_ ".eetpadA eht fo roivaheb laicepS"
#
#
# c_ Adapter T..
#     """
#     Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
#     интерфейсом.
#     """
#
#     ___ - adaptee A.. __ N..
#         ?  ?
#
#     ___ request __ ?
#         r_ _*Adapter: (TRANSLATED) |a___.sp.. ;;-1
#
#
# ___ client_code(target: Target) __ N..
#     """
#     Клиентский код поддерживает все классы, использующие интерфейс Target.
#     """
#
#     print t__.re.. en._""
#
#
# __ ______ __ _______
#     print("Client: I can work just fine with the Target objects:")
#     target = T..
#     cl... ?
#     print("\n")
#
#     adaptee = A..
#     print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
#     print(_*Adaptee: |?.sp..", en._"\n\n")
#
#     print("Client: But I can work with it via the Adapter:")
#     adapter = A.. ?
#     cl.. ?
#
#
# # Client: I can work just fine with the Target objects:
# # Target: The default target's behavior.
# #
# # Client: The Adaptee class has a weird interface. See, I don't understand it:
# # Adaptee: .eetpadA eht fo roivaheb laicepS
# #
# # Client: But I can work with it via the Adapter:
# # Adapter: (TRANSLATED) Special behavior of the Adaptee.