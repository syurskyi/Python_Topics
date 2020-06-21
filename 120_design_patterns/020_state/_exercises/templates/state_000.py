# # -*- coding: utf-8 -*-
#
# ____ -f ______ a...
# ____ a.. ______ A.. a..
#
#
# c_ Context A..
#     """
#     Контекст определяет интерфейс, представляющий интерес для клиентов. Он также
#     хранит ссылку на экземпляр подкласса Состояния, который отображает текущее
#     состояние Контекста.
#     """
#
#     _state _ N..
#     """
#     Ссылка на текущее состояние Контекста.
#     """
#
#     ___  - state S.. __ ?
#         t_t. ?
#
#     ___ transition_to  state S..
#         """
#         Контекст позволяет изменять объект Состояния во время выполнения.
#         """
#
#         print _*Context: Transition to |ty.. ? . -n
#         _?  ?
#         _?.c.. _ ?
#
#     """
#     Контекст делегирует часть своего поведения текущему объекту Состояния.
#     """
#
#     ___ request1
#         _?.h_1
#
#     ___ request2
#         _?.h_2
#
#
# c_ State A..
#     """
#     Базовый класс Состояния объявляет методы, которые должны реализовать все
#     Конкретные Состояния, а также предоставляет обратную ссылку на объект
#     Контекст, связанный с Состоянием. Эта обратная ссылка может использоваться
#     Состояниями для передачи Контекста другому Состоянию.
#     """
#
#     ??
#     ___ context __ C..
#         r_ _context
#
#     ??.?
#     ___ context  context C.. __ ?
#         _?  ?
#
#     ??
#     ___ handle1(self) __ ?
#         p..
#
#     ??
#     ___ handle2 __ ?
#         p..
#
#
# """
# Конкретные Состояния реализуют различные модели поведения, связанные с
# состоянием Контекста.
# """
#
#
# c_ ConcreteStateA S..
#     ___ handle1 __ ?
#         print("ConcreteStateA handles request1.")
#         print("ConcreteStateA wants to change the state of the context.")
#         c___.t_t. C_B
#
#     ___ handle2 __ ?
#         print("ConcreteStateA handles request2.")
#
#
# c_ ConcreteStateB S..
#     ___ handle1 __ ?
#         print("ConcreteStateB handles request1.")
#
#     ___ handle2 __ ?
#         print("ConcreteStateB handles request2.")
#         print("ConcreteStateB wants to change the state of the context.")
#         c____.t_t. C_A
#
#
# __ ________ __ _______
#     # Клиентский код.
#
#     context _ C... C_A
#     ?._1
#     ?._2