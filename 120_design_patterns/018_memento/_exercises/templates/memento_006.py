# # coding: utf-8
#
# """
# Хранитель (Memento) - паттерн поведения объектов.
#
# Не нарушая инкапсуляции, фиксирует и выносит за пределы объекта его внутреннее состояние так,
# чтобы позднее можно было восстановить в нем объект.
# """
#
#
# c_ Memento o..
#     """Хранитель"""
#     ___ - state
#         _?  ?
#
#     ___ get_state
#         r_ _state
#
#
# c_ Caretaker o..
#     """Опекун"""
#     ___ -
#         _memento _ N..
#
#     ___ get_memento
#         r_ _?
#
#     ___ set_memento memento
#         _?  ?
#
#
# c_ Originator o..
#     """Создатель"""
#     ___ -
#         _state _ N..
#
#     ___ set_state state
#         _?  ?
#
#     ___ get_state
#         r_ _?
#
#     ___ save_state
#         r_ M.. _s..
#
#     ___ restore_state memento
#         _state _ m___.g_s..
#
#
# originator _ O..
# caretaker _ C..
#
# o___.s_s.. 'on'
# print 'Originator state:', o___.g_s..  # Originator state: on
# c___.s_m... o__.s_s..
#
# o___.s_s.. 'off'
# print 'Originator change state:', o___.g_s..  # Originator change state: off
#
# o____.r_s.. c___.g_m..
# print 'Originator restore state:', o_____.g_s..    # Originator restore state: on
