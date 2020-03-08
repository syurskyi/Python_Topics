# # -*- coding: utf-8 -*-
#
# ____ -f ______ a...
# ____ a.. ______ A.. a..
# ____ d_t_ ______ d_t_
# ____ ra.. ______ s..
# ____ str..______ a_l.. dig..
#
#
# c_ Originator
#     """
#     Создатель содержит некоторое важное состояние, которое может со временем
#     меняться. Он также объявляет метод сохранения состояния внутри снимка и
#     метод восстановления состояния из него.
#     """
#
#     _state _ N..
#     """
#     Для удобства состояние создателя хранится внутри одной переменной.
#     """
#
#     ___ - state ? __ ?
#         _?  ?
#         print _*Originator: My initial state is: |_?")
#
#     ___ do_something __ ?
#         """
#         Бизнес-логика Создателя может повлиять на его внутреннее состояние.
#         Поэтому клиент должен выполнить резервное копирование состояния с
#         помощью метода save перед запуском методов бизнес-логики.
#         """
#
#         print("Originator: I'm doing something important.")
#         _state _ _g_r_s.. 30
#         print _*Originator: and my state has changed to: |_?")
#
#     ___ _generate_random_string length int _ 10 __ ?
#         r_ "".jo.. sa.. a_l.. l..
#
#     ___ save __ M..
#         """
#         Сохраняет текущее состояние внутри снимка.
#         """
#
#         r_ CM... _s..
#
#     ___ restore memento M... __ ?
#         """
#         Восстанавливает состояние Создателя из объекта снимка.
#         """
#
#         _state _ m___.g_s..
#         print _*Originator: My state has changed to: |_s..
#
#
# c_ Memento A..
#     """
#     Интерфейс Снимка предоставляет способ извлечения метаданных снимка, таких
#     как дата создания или название. Однако он не раскрывает состояние Создателя.
#     """
#
#     ??
#     ___ get_name __ ?
#         p..
#
#     ??
#     ___ get_date __ ?:
#         p..
#
#
# c_ ConcreteMemento M..
#     ___ - state ?) __ ?
#         _?  ?
#         _date _ st. d_t_.no.|;19
#
#     ___ get_state __ ?:
#         """
#         Создатель использует этот метод, когда восстанавливает своё состояние.
#         """
#         r_ _s..
#
#     ___ get_name __ ?:
#         """
#         Остальные методы используются Опекуном для отображения метаданных.
#         """
#
#         r_ _*|_d.. / ||_s..|0;9...)"
#
#     ___ get_date __ ?
#         r_ _d..
#
#
# c_ Caretaker
#     """
#     Опекун не зависит от класса Конкретного Снимка. Таким образом, он не имеет
#     доступа к состоянию создателя, хранящемуся внутри снимка. Он работает со
#     всеми снимками через базовый интерфейс Снимка.
#     """
#
#     ___ - originator O.. __ ?
#         _mementos _     # list
#         _?  ?
#
#     ___ backup __ ?
#         print("\nCaretaker: Saving Originator's state...")
#         _m___.ap.. _o____.s..
#
#     ___ undo __ ?
#         __ no. le. _m..
#             r_
#
#         memento _ _m__.po.
#         print _*Caretaker: Restoring state to: |m___.g_n..
#         ___
#             _o___.re.. ?
#         _______ E..
#             un..
#
#     ___ show_history __ ?
#         print("Caretaker: Here's the list of mementos:")
#         ___ memento in _m..
#             print ?.g_n..
#
#
# __ _______ __ ______
#     originator _ O.. "Super-duper-super-puper-super."
#     caretaker _ C.. ?
#
#     ?.ba..
#     o____.d_s..
#
#     c___.ba...
#     o____.d_s..
#
#     c___.ba...
#     o____.d_s..
#
#     print()
#     c___.s_h...
#
#     print("\nClient: Now, let's rollback!\n")
#     c___.u..
#
#     print("\nClient: Once more!\n")
#     c___.u..
#
#
# # Originator: My initial state is: Super-duper-super-puper-super.
# #
# # Caretaker: Saving Originator's state...
# # Originator: I'm doing something important.
# # Originator: and my state has changed to: wQAehHYOqVSlpEXjyIcgobrxsZUnat
# #
# # Caretaker: Saving Originator's state...
# # Originator: I'm doing something important.
# # Originator: and my state has changed to: lHxNORKcsgMWYnJqoXjVCbQLEIeiSp
# #
# # Caretaker: Saving Originator's state...
# # Originator: I'm doing something important.
# # Originator: and my state has changed to: cvIYsRilNOtwynaKdEZpDCQkFAXVMf
# #
# # Caretaker: Here's the list of mementos:
# # 2019-01-26 21:11:24 / (Super-dup...)
# # 2019-01-26 21:11:24 / (wQAehHYOq...)
# # 2019-01-26 21:11:24 / (lHxNORKcs...)
# #
# # Client: Now, let's rollback!
# #
# # Caretaker: Restoring state to: 2019-01-26 21:11:24 / (lHxNORKcs...)
# # Originator: My state has changed to: lHxNORKcsgMWYnJqoXjVCbQLEIeiSp
# #
# # Client: Once more!
# #
# # Caretaker: Restoring state to: 2019-01-26 21:11:24 / (wQAehHYOq...)
# # Originator: My state has changed to: wQAehHYOqVSlpEXjyIcgobrxsZUnat