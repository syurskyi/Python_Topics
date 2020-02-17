# ____ a.. _______ A..
#
#
# c_ Shape ?
#     ___ -s
#         r_ ''
#
#
# c_ Circle S..
#     ___ -  radius_0.0
#         ?  ?
#
#     ___ resize  factor
#         ?r.. *= ?
#
#     ___ -s
#         r_ _*A circle of radius |?r..
#
#
# c_ Square S..
#     ___ -i side
#         ?  ?
#
#     ___ -s
#         r_ _*A square with side |?s..'
#
#
# c_ ColoredShape S..
#     ___ -  shape color
#         __ isi... ? C..
#             r_ E.. ('Cannot apply ColoredDecorator twice')
#         ?  ?
#         ?  ?
#
#     ___ -s
#         r_ _*|?s..| has the color |?c..
#
#
# c_ TransparentShape S..
#     ___ - shape transparency
#         ?  ?
#         ?  ?
#
#     ___ -s
#         r_ _*|?s..| has |?t.. * 100.0|% transparency'
#
#
# __ _______ __ ______
#     circle = C.. 2
#     print ?
#
#     red_circle = CS.. ? "red"
#     print ?
#
#     # ColoredShape doesn't have resize()
#     # red_circle.resize(3)
#
#     red_half_transparent_square = TS_ ? 0.5
#     print ?
#
#     # nothing prevents double application
#     mixed = CS.. CS.. C.. 3 'red' 'blue'
#     print ?
