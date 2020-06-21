# # -*- coding: utf-8 -*-
# ___ a ______ A.. a..
#
# # Abstract Class
#
# c_ SpeedControl o..
#
#     ??
#     ___ start_engine
#         r_ N..
#
#     ??
#     ___ accelerate
#         r_ N..
#
#     ??
#     ___ brake
#         r_ N..
#
#     ??
#     ___ change_gear
#         r_ N..
#
# c_ RadioCd o..
#
#     ??
#     ___ stop_radio
#         r_ N..
#
#     ??
#     ___ eject_cd
#         r_ N..
#
# # implements
#
# c_ CarSpeedControl S..
#
#     ___ start_engine
#         print('start engine')
#
#     ___ accelerate
#         print('accelerate')
#
#     ___ brake
#         print('brake')
#
#     ___ change_gear
#         print('change gear')
#
# c_ CarRadioCd R..
#
#     ___ stop_radio
#         print('stop radio')
#
#     ___ eject_cd
#         print('eject cd')
#
# # Decorator
#
# ___ validate_type_hinting func
#     ___ inner(*argv):
#         __ no. iss.. ty.. ar.. 1 S... : print("@ is a type @, the function need a SpeedControl type"  ar.. 1 ty.. ar.. 1||||; exit(0)
#         __ no. iss.. ty.. ar.. 2 R... : print("@ is a type @, the function need a RadioCd type"  ar.. 2 ty.. ar.. 2||||; exit(0)
#         r_ f.. $
#     r_ i..
#
# # Vehicle
#
# c_ Car o..
#
#     ?v...
#     ___ - speed_control radio_cd
#         ??  ?
#         ??  ?
#
# __ ______ __ _______
#     speed_control = CSC..
#     radio_cd = CRC...
#     car = C.. ?  ?
#     ?.s_c_.s_e..
#     ?.s_c_.a...
