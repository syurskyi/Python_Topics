# # Liskov Substitution Principle (LSP)
#
# # Functions that use references to base classes must be able to use any object of derived classes without knowing it.
#
# # Consequence: Sometimes something "is a" in the real world but should not be an "is a" in the code
#
#
# c_ Rectangle:
#     ___ -  name ? width: f.. height f..
#         ??  ?
#         _?  ?
#         _?  ?
#
#     ___ -s
#         r_ _*|n.. : |_w.. x|_h.. "
#
#     ___ double_height
#         _h.. *_ 2
#
#     ___ double_width
#         _w.. *_ 2
#
#     ?p..
#     ___ is_square __ b..
#         r_ _w.. __ _h...
#
#
# c_ Square R..
#     ___ -  name ? side f..
#         s___.- ? ? side
#
#     ___ double_height
#         _h.. *_ 2
#         _w.. *_ 2
#
#     ___ double_width
#         _w.. *_ 2
#         _h.. *_ 2
#
#
# ___ double_size rectangle R.. __ N..
#     ?.d_h..
#     ?.d_w..
#
#
# __ _______ __ _______
#     rectangle = R.. "My Rectangle", 3, 2
#     print ?
#
#     # rectangle.double_height()
#     d_s.. ?
#     print ?
#
#     square = S.. "My Square", 3
#     print ?
#
#     # square.double_height()
#     d_s.. ?
#     print ?
