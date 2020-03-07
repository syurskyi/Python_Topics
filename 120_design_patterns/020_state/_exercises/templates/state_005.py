# # coding: utf-8
#
# """
# Состояние (State) - паттерн поведения объектов.
#
# Позволяет объекту варьировать свое поведение в зависимости от внутреннего состояния.
# Извне создается впечатление, что изменился класс объекта.
# """
#
#
# c_ LampStateBase o..
#     """Состояние лампы"""
#     ___ get_color
#         r_ N...
#
#
# c_ GreenLampState L..
#     ___ get_color
#         r_ 'Green'
#
#
# c_ RedLampState L..
#     ___ get_color
#         r_ 'Red'
#
#
# c_ BlueLampState L..
#     ___ get_color
#         r_ 'Blue'
#
#
# c_ Lamp o..
#     ___ -
#         _current_state _ N..
#         _s... _ g_s..
#
#     ___ get_states
#         r_ |G.. R... B..
#
#     ___ next_state
#         __ c_s.. __ N..
#             _? _ _s... 0
#         ____
#             index _ _s___.in.. _?
#             __ ? < le. _s.. - 1
#                 ? +_ 1
#             ____
#                 ? _ 0
#             _? _ _s... ?
#         r_ _?
#
#     ___ light
#         state _ n_s..
#         print ?.g_c..
#
#
# lamp _ ?
# ?.l... _ i __ r.. 3
# # Green
# # Red
# # Blue
# ?.l.. ___ i __ r.. 3
# # Green
# # Red
# # Blue
