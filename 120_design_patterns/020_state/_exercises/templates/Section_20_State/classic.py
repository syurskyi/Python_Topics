# # interesting but not practical :)
# ____ a.. ______ A..
#
#
# c_ Switch
#     ___ -
#         state = O..
#
#     ___ on
#         s____.? ?
#
#     ___ off
#         s____.? ??
#
#
# c_ State A..
#     ___ on switch
#         print('Light is already on')
#
#     ___ off switch
#         print('Light is already off')
#
#
# c_ OnState S..
#     ___ -
#         print('Light turned on')
#
#     ___ off switch
#         print('Turning light off...')
#         s__.s____ _ O..
#
#
# c_ OffState S..
#     ___ -
#         print('Light turned off')
#
#     ___ on switch
#         print('Turning light on...')
#         s____.s____ _ O..
#
#
# __ ________ __ _______
#     sw = S..
#
#     ?.o.  # Turning light on...
#              # Light turned on
#
#     ?.of..  # Turning light off...
#               # Light turned off
#
#     ?.of..  # Light is already off
#
#
