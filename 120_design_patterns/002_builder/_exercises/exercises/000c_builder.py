# # coding: utf-8
# 
# 
# c_ Builder o..
#     ___ build_body
#         r_ N...
# 
#     ___ build_lamp
#         r_ N...
# 
#     ___ build_battery
#         r_ N...
# 
#     ___ create_flashlight
#         r_ N...
# 
# 
# c_ Flashlight o..
#     """Карманный фонарик"""
# 
#     ___ - body lamp battery
#         _shine _ F..  # излучать свет
#         _?  ?
#         _?  ?
#         _?  ?
# 
#     ___ on
#         _sh.. _ T..
# 
#     ___ off
#         _shine _ F..
# 
#     ___ -s
#         shine _ 'o.' __ _s.. ____ 'of.'
#         r_ 'Flashlight [@]'  ?       # string
# 
# 
# c_ Lamp o..
#     """Лампочка"""
# 
# 
# c_ Body o..
#     """Корпус"""
# 
# 
# c_ Battery o..
#     """Батарея"""
# 
# 
# c_ FlashlightBuilder B..
#     ___ build_body
#         r_ B..
# 
#     ___ build_battery
#         r_ B..
# 
#     ___ build_lamp
#         r_ L..
# 
#     ___ create_flashlight
#         body _ b..
#         lamp _ b..
#         battery _ b..
#         r_ F.. ?  ?  ?
# 
# 
# builder _ F..
# flashlight _ ?.c..
# ?.o.
# print ? # Flashlight [on]
