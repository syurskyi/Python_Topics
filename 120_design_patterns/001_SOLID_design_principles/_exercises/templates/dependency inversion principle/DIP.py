# # Dependence Inversion Principle, DIP for short
#
# ____ a.. ______ A.. a..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ Animal m..
#     """animal"""
#
#     ___ - name
#         _?  ?
#
#     ___ eat food
#         __ ?cF.. ?
#             print(_n.. + "Eat" + f__.gN..
#         ____
#             print(_n.. + "Not eat" + f__.gN..
#
#     ??
#     ___ checkFood food
#         """Check what foods you can eat"""
#         p..
#
#
# c_ Dog A..
#     """dog"""
#
#     ___ -
#         s__. -("d..
#
#     ___ checkFood food
#         r_ f___.ca.. __ "me..
#
#
# c_ Swallow A..
#     """Swallow"""
#
#     ___  -
#         s__. -("Sw..
#
#     ___ checkFood food
#         r_ f___.ca.. __ "in..
#
#
# c_ Food m..
#     """food"""
#
#     ___  -  name
#         _?  ?
#
#     ___ getName
#         r_ _n..
#
#     ??
#     ___ category
#         """Food category"""
#         p..
#
#     ??
#     ___ nutrient
#         """nutrient content"""
#         p..
#
#
# c_ Meat F..
#     """meat"""
#
#     ___  -:
#         s__. - "m..
#
#     ___ category
#         r_ "m..
#
#     ___ nutrient
#         r_ "Protein, fat"
#
#
# c_ Worm F..
#     """insect"""
#
#     ___  -
#         s__. - "i..
#
#     ___ category
#         r_ "i..
#
#     ___ nutrient
#         r_ "Protein and trace elements"
#
#
# ___ Food
#     dog = D..
#     swallow = S..
#     meat = M..
#     worm = W..
#     d__.e.. m..
#     d__.e.. w..
#     s__.e.. m..
#     s__.e.. w..
#
#
# Food()