# """Coding Challenge #2
# """
#
#
# c_ Car
#     ___ -
#         _speed _ 0
#         _start_car _ F..
#
#     ___ start_car
#         __ ?:
#             r_ E.. "The car is already on"
#         ? _ T..
#
#     ___ turn_off_car
#         __ ? !_ 0
#             r_ E.. "Cannot turn off car because of speed"
#         ? _ F..
#
#     ___ add_speed
#         ? +_ 5
#
#     ___ remove_speed
#         __ ? <_ 0
#             ? _ 0
#         ____
#             ? -_ 5
#
#     ___ current_speed
#         r_ ?
#
#     ___ stop
#         ? _ 0
#
#     ___ car_status
#         r_ ?