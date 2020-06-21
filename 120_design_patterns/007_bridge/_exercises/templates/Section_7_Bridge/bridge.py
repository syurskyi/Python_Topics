# # Circles and squares
# # Each can be rendered in vector or raster form
#
# c_ Renderer
#     ___ render_circle radius
#         p..
#
#
# c_ VectorRenderer R..
#     ___ render_circle radius
#         print _*Drawing a circle of radius |?')
#
#
# c_ RasterRenderer R..
#     ___ render_circle radius
#         print _*Drawing pixels for circle of radius |?')
#
#
# c_ Shape
#     ___ - renderer
#         ?  ?
#
#     ___ draw p..
#     ___ resize factor p..
#
#
# c_ Circle S..
#     ___ - renderer radius
#         s__. - ?
#         ?  ?
#
#     ___ draw
#         r___.r_c.. r..
#
#     ___ resize factor
#         r.. *_ ?
#
#
# __ _______ __ ______k
#     raster = ?
#     vector = ?
#     circle = ? vector, 5
#     c___.d..
#     c___.r.. 2
#     c___.d..