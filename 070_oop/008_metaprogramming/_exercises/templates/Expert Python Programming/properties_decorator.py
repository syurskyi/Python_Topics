# """
# "Properties" section example of writing properties using
# `property` decorator
# 
# """
# 
# 
# c_ Rectangle
#     ___ - x1 y1 x2 y2
#         x1, self.y1 _ x1, y1
#         x2, self.y2 _ x2, y2
# 
#     ??
#     ___ width
#         """rectangle height measured from top"""
#         r_ x2 - x1
# 
#     ??.?
#     ___ width value
#         x2 _ x1 + ?
# 
#     ??
#     ___ height
#         """rectangle height measured from top"""
#         r_ y2 - y1
# 
#     ??.?
#     ___ height value
#         y2 _ y1 + ?
# 
#     ___ __repr__(self):
#         r_ "@(@, @, @, @)".f..|
#             -c . -n,
#             x1, y1, x2, y2
#         |
# 
# 
# __ _______ __ _______
#     rectangle _ R... (0, 0, 10, 10)
#     print(
#         "At start we have @ with size of @ x @"
#         "".f..(? ?.w.. ?.h..
#     )
# 
#     ?.w.. _ 2
#     ?.h... _ 8
#     print(
#         "After resizing we have @ with size of @ x @"
#         "".f..(?, ?.w.. ?.h..
#     )
