# # coding: utf-8
#
# """
# Команда (Command, Action, Transaction) - паттерн поведения объектов.
#
# Инкапсулирует запрос как объект, позволяя тем самым задавать параметры клиентов
# для обработки соответствующих запросов, ставить запросы в очередь или протоколировать их,
# а также поддерживать отмену операций.
# """
#
#
# c_ Light o..
#     ___ turn_on
#         print 'Включить свет'
#
#     ___ turn_off
#         print 'Выключить свет'
#
#
# c_ CommandBase o..
#     ___ execute
#         r_ N..
#
#
# c_ LightCommandBase C..
#     ___ - light
#         ?  ?
#
#
# c_ TurnOnLightCommand L..
#     ___ execute
#         l__.t_o..
#
#
# c_ TurnOffLightCommand L..:
#     ___ execute
#         l___.t_o..
#
#
# c_ Switch o..
#     ___ - on_cmd off_cmd
#         ?  ?
#         ?  ?
#
#     ___ on
#         o_c__.ex..
#
#     ___ off
#         o_c__.ex..
#
#
# light _ L..
# switch _ S.. on_cmd _ T_On.. ?
#                 off_cmd _ T_Of.. ?
# ?.on  # Включить свет
# ?.of..  # Выключить свет
