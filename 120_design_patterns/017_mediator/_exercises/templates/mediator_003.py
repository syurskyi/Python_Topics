# # coding: utf-8
#
# """
# Посредник (Mediator) - паттерн поведения объектов.
#
# Определяет объект, инкапсулирующий способ взаимодействия множества объектов.
# Посредник обеспечивает слабую связанность системы, избавляя объекты от необъодимости явно ссылаться друг на друга
# и позволяя тем самым независимо изменять взаимодействия между ними.
# """
#
#
# c_ WindowBase o..
#     ___ show
#         r_ N...
#
#     ___ hide
#         r_ N...
#
#
# c_ MainWindow W..
#     ___ show
#         print 'Show MainWindow'
#
#     ___ hide
#         print 'Hide MainWindow'
#
#
# c_ SettingWindow W..
#     ___ show
#         print 'Show SettingWindow'
#
#     ___ hide
#         print 'Hide SettingWindow'
#
#
# c_ HelpWindow W..
#     ___ show
#         print 'Show HelpWindow'
#
#     ___ hide
#         print 'Hide HelpWindow'
#
#
# c_ WindowMediator o..
#     ___ -
#         windows _ di__.f_k..'main', 'setting', 'help'
#
#     ___ show win
#         ___ window __ w___.it__v..
#             __ no. ? __ ?
#                 ?.h..
#         ?.sh..
#
#     ___ set_main win
#         windows|*main _ ?
#
#     ___ set_setting win
#         windows|*setting _ ?
#
#     ___ set_help win
#         windows|*help _ ?
#
#
# main_win _ M..
# setting_win _ S..
# help_win _ H..
#
# med _ WM..
# ?.s_m.. m_w..
# ?.s_s.. s_w..
# ?.s_h.. h_w..
#
# m_w__.sh..  # Show MainWindow
#
# ?.sh.. s_w..
# # Hide MainWindow
# # Hide HelpWindow
# # Show SettingWindow
#
# ?.sh.. h_w..
# # Hide MainWindow
# # Hide SettingWindow
# # Show HelpWindow
