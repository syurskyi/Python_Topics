# """
# "Properties" section example of writing properties as separate
# access methods with class level call to `property()` function.
#
# """
#
#
# c_ Rectangle
#     ___ -  x1 y1 x2 y2
#         x1 y1 _ x1 y1
#         x2 y2 _ x2 y2
#
#     ___ _width_get
#         r_ x2 - x1
#
#     ___ _width_set value
#         x2 _ x1 + ?
#
#     ___ _height_get
#         r_ y2 - y1
#
#     ___ _height_set value
#         y2 _ y1 + ?
#
#     width _ p... |
#         _? _?
#         doc_"rectangle width measured from left"
#     |
#     height _ p... |
#         _? _?
#         doc_"rectangle height measured from top"
#     |
#
#     ___ -r
#         r_ "@(@ @ @ @)".f..|
#             -c. -n
#             x1 y1 x2 y2
#         |
#
#
# __ _______ __ _______
#     rectangle _ R...(0 0 10 10)
#     print|
#         "At start we have @ with size of @ x @"
#         "".f.. ? ?.w.. ?.h..
#     |
#
#     ?.w.. _ 2
#     ?.h.. _ 8
#     print(
#         "After resizing we have @ with size of @ x @"
#         "".f.. ? ?.w.. ?.h..
#     ?
