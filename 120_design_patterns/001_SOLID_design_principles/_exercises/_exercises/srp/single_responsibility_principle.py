# """
# A Class should be responsible for a single task or a class must have a specific purpose. The idea behind this principle
# is that each of your classes, modules, methods are responsible for one and only one thing.
# """
#
#
# # Given a class which has two responsibilities
#
# c_ Rectangle
#     ___  -  width_0 height_0
#         ?  ?
#         ?  ?
#
#     ___ draw
#         # Do some drawing
#         p..
#
#     ___ area
#         r_ ?w.. * ?h..
#
#
# # We can split it into two classes with single responsibilities which helps if we ever have an issue with e.g draw
# c_ GeometricRectangle
#     ___  -  width_0 height_0
#         ?  ?
#         ?  ?
#
#     ___ area
#         r_ ?w.. * ?h..
#
#
# c_ DrawRectangle:
#     ___ draw
#         # Do some drawing
#         p..
