# # -*- coding: utf-8 -*-
#
# ____ -f ______ a..
# ____ a.. ______ A..
#
#
# c_ Mediator A..
#     """
#     Интерфейс Посредника предоставляет метод, используемый компонентами для
#     уведомления посредника о различных событиях. Посредник может реагировать на
#     эти события и передавать исполнение другим компонентам.
#     """
#
#     ___ notify sender object event ? __ ?
#         p..
#
#
# c_ ConcreteMediator M...
#     ___ - component1 C_1 component2 C_2 __ ?
#         _?  ?
#         _component1.m___ _ ?
#         _?  ?
#         _c_2.m___ _ ?
#
#     ___ notify sender object event ? __ ?
#         __ e.... __ "A":
#             print("Mediator reacts on A and triggers following operations:")
#             _component2.d._c
#         ____ e.... __ "D":
#             print("Mediator reacts on D and triggers following operations:")
#             _c_1.d._b
#             _c_2.d._c
#
#
# c_ BaseComponent
#     """
#     Базовый Компонент обеспечивает базовую функциональность хранения экземпляра
#     посредника внутри объектов компонентов.
#     """
#
#     ___ - mediator M.. _ N... __ ?
#         _?  ?
#
#     ??
#     ___ mediator __ M..
#         r_ _m..
#
#     ??.?
#     ___ m___ m____ M.. __ ?
#         _m... _ m...
#
#
# """
# Конкретные Компоненты реализуют различную функциональность. Они не зависят от
# других компонентов. Они также не зависят от каких-либо конкретных классов
# посредников.
# """
#
#
# c_ Component1 B..
#     ___ do_a __ ?
#         print("Component 1 does A.")
#         m___.n.. "A")
#
#     ___ do_b __ ?
#         print("Component 1 does B.")
#         m___.n.."B")
#
#
# c_ Component2(BaseComponent):
#     ___ do_c __ ?
#         print("Component 2 does C.")
#         m___.n.. "C")
#
#     ___ do_d __ ?
#         print("Component 2 does D.")
#         m___.n.. "D")
#
#
# __ _______ __ ______
#     # Клиентский код.
#     c1 _ C_1
#     c2 _ C_2
#     m___ _ CM..?  ?
#
#     print("Client triggers operation A.")
#     c1.d._a
#
#     print("\n", e.._"")
#
#     print("Client triggers operation D.")
#     c2.d._d
#
# # Client triggers operation A.
# # Component 1 does A.
# # Mediator reacts on A and triggers following operations:
# # Component 2 does C.
# #
# #
# # Client triggers operation D.
# # Component 2 does D.
# # Mediator reacts on D and triggers following operations:
# # Component 1 does B.
# # Component 2 does C.