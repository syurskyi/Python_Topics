# # Lazy Iterables
#
# # Lazy evaluation is when evaluating a value is deferred until it is actually requested.
# # Simple examples of lazy evaluation are often seen in classes for calculated properties.
# # As you can see, in this circle class, every time we set the radius, we re-calculate and store the area.
# # When we request the area of the circle, we simply return the stored value.
#
# ______ ma..
#
# c___ Circle
#     ___ __init__ ____ r
#         ____.radius _ r
#
#     0p..
#     ___ radius ____
#         return ____._radius
#
#     0r__.s...
#     ___ radius ____ r
#         ____._radius _ r
#         ____.area _ ma__.pi * r ** 2
#
#
# c _ C... 1
# c.area
# c.radius = 2
# c.radius, c.area
#
# # Simple examples of lazy evaluation are often seen in classes for calculated properties.
# #
# # But instead of doing it this way, we could just calculate the area every time
# # it is requested without actually storing the value
#
# c___ Circle
#     ___ __i... ____ r
#         ____.radius _ r
#
#     0p..
#     ___ radius ____
#         r_ ____._radius
#
#     0r__.s..
#     ___ radius ____, r
#         ____._radius _ r
#
#     0p..
#     ___ area ____
#         r_ m__.pi * ____.ra__ ** 2
#
#
# c _ C... 1
# c.area
# c.radius _ 2
# c.area
#
#
# # Simple examples of lazy evaluation are often seen in classes for calculated properties.
#
# c___ Circle
#     ___ __init__ ____ r
#         ____.radius _ r
#
#     0p..
#     ___ radius ____
#         r_ ____._radius
#
#     0r__.s...
#     ___ radius ____ r
#         ____._radius _ r
#         ____._area _ N..
#
#     0p..
#     ___ area ____
#         i_ ____._area i. N..
#             print Calculating area...
#             ____._area _ ma__.pi * ____.radius ** 2
#         r_ ____._area
#
#
# c _ Circle 1
# c.area
# c.area
# c.radius _ 2
# c.area
