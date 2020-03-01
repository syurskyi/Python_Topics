# # Interface Segregation Principle (ISP)
#
# # No client should be forced to depend on methods it doesn't use
#
#
# ____ a.. ______ A.. a..
# ____ e.. ______ E..
# ____ ty.. ______ L..
#
#
# c_ Color E..
#     RED = "red"
#     GREEN = "green"
#     ORANGE = "orange"
#     BLUE = "blue"
#
#
# c_ ColoredShape A..
#     ___ - color C..
#         ??  ?
#
#
# c_ ShapeWithArea A..
#     ?p..
#     ?a..
#     ___ area __ ?
#         p..
#
#
# c_ OpenCircle CS..
#     ___ -s
#         r_ _*|?c__.v..| circle
#
#
# c_ Rectangle S.. C..
#     ___ - color C.. width ? height ?
#         s__ . - c..
#         w.. _ w..
#         h.. _ h..
#
#     ?p..
#     ___ area __ ?
#         r_ w.. * h..
#
#     ___ -s
#         r_ _*|?c__.v..| rectangle with an area of |?a..|"
#
#
# c_ Square S.. C..
#     ___ - color C.. side ?
#         s__ . - c..
#         s.. _ s..
#
#     ?p..
#     ___ area __ ?
#         r_ .s.. * .s..
#
#     ___ -s
#         r_ _*|.c__.v..| square with an area of |.a..|"
#
#
# ___ blue_filter shapes L.. C..|S..
#     ___ shape __ ?
#         __ ?.c.. __ C__.B..
#             y.. ?
#
#
# ___ area_filter shapes L..|S.. max_area ?
#     ___ shape __ ?
#         __ ?.a.. <_ m..
#             y.. ?
#
#
# __ ______ __ ______
#     rectangle _ R.. C__.B.. 3.0, 2.0
#     print ?
#
#     square _ S.. C__.G.. 3.0
#     print ?
#
#     open_circle _ O.. C__.B..
#     print ?
#
#     blue_shapes = b_f.. ?  ?  ?
#     ___ blue_shape __ ?
#         print ?
