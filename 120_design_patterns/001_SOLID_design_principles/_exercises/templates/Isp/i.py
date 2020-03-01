# """
# Interface Segregation Principle
#
#
# bad - Circle class does not need draw_rectangle and draw_square.
#
# if we want to add new shapes, we have to change all classes.
# """
#
#
# c_ IShape
#     ___ draw_square
#         r_ N..
#
#     ___ draw_rectangle
#         r_ N..
#
#     ___ draw_circle
#         r_ N..
#
#
# c_ Circle IS..
#     ___ draw_square
#         p..
#
#     ___ draw_rectangle
#         p..
#
#     ___ draw_circle
#         p..
#
#
# c_ Square IS..
#     ___ draw_square
#         p..
#
#     ___ draw_rectangle
#         p..
#
#     ___ draw_circle
#         p..
#
#
# c_ Rectangle IS..
#     ___ draw_square
#         p..
#
#     ___ draw_rectangle
#         p..
#
#     ___ draw_circle
#         p..
#
#
# """
# better
#
#
# draw segregate to different interfaces.
# """
#
#
# c_ IShape
#     ___ draw
#         r_ N..
#
#
# c_ Circle IS..
#     ___ draw
#         p..
#
#
# c_ Square IS..
#     ___ draw
#         p..
#
#
# c_ Rectangle IS..
#     ___ draw
#         p..
#
