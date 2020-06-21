# # Implementor
# c_ DrawingAPI
#     ___ drawCircle x y radius
#         p..
#
#
# # ConcreteImplementor 1/2
# c_ DrawingAPI1 D..
#     ___ drawCircle x y radius
#             print "API1.circle at @:@ radius @"  ?  ?  ?
#
#
# # ConcreteImplementor 2/2
# c_ DrawingAPI2 D..
#     ___ drawCircle self x, y radius)
#             print "API2.circle at @:@ radius @"  ?  ?  ?
#
#
# # Abstraction
# c_ Shape
#     # Low-level
#     ___ draw
#         p..
#
#     # High-level
#     ___ resizeByPercentage pct
#         p..
#
#
# # Refined Abstraction
# c_ CircleShape S..
#     ___ - x y radius drawingAPI
#         __?  ?
#         __?  ?
#         __?  ?
#         __?  ?
#
#     # low-level i.e. Implementation specific
#     ___ draw
#         __dAP_.dC.. __x __y __r..
#
#     # high-level i.e. Abstraction specific
#     ___ resizeByPercentage pct
#         __r.. *_ ?
#
#
# ___ main
#     shapes = |
#         CS..(1, 2, 3, D_1,
#         CS..(5, 7, 11, D_2
#     |
#
#     ___ shape __ ?
#         ?.rBP..(2.5)
#         ?.d..
#
# __ ______ __ ______
#     ?
