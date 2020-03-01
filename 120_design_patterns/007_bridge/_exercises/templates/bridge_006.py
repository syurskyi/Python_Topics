# # coding: utf-8
#
# """
# Мост (Bridge) - паттерн, структурирующий объекты.
#
# Основная задача - отделить абстракцию от её реализации так,
# чтобы то и другое можно было изменять независимо.
# """
#
#
# c_ TVBase o..
#     """Абстрактный телевизор"""
#     ___ tune_channel channel
#         r_ N...
#
#
# c_ SonyTV T..
#     """Телевизор Sony"""
#     ___ tune_channel channel
#         print('Sony TV: выбран @ канал'  ?
#
#
# c_ SharpTV T
#     """Телевизор Sharp"""
#     ___ tune_channel channel
#         print('Sharp TV: выбран @ канал'  ?
#
#
# c_ RemoteControlBase o..
#     """Абстрактный пульт управления"""
#     ___ -
#         _tv _ .g_t.
#
#     ___ get_tv
#         r_ N...
#
#     ___ tune_channel channel
#         _t_.t_c.. ?
#
#
# c_ RemoteControl R..
#     """Пульт управления"""
#     ___ -
#         s___ ? ____. -
#         _c.. _ 0  # текущий канал
#
#     ___ get_tv(
#         r_ S..
#
#     ___ tune_channel channel
#         s___ ? ____ .t_c.. ?
#         _?  ?
#
#     ___ next_channel
#         _c.. +_ 1
#         t_c.. _c..
#
#     ___ previous_channel
#         _c.. -_ 1
#         t_c.. _c..
#
#
# remote_control _ R...
# ?.t_c.. 5  # Sharp TV: выбран 5 канал
# ?.n_c..  # Sharp TV: выбран 6 канал
