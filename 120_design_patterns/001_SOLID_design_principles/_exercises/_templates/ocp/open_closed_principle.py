# """
# A class should be easily extendable without modifying the class itself
#
# In Python we are able to change the functionality of any method, class or function at will. We can even add methods to
# classes (or individual instances!) at run-time. For example, imagine we had created a GeometricRectangle using our
# previous example, but in order to make it fit into a badly designed API which insisted on the object having a name()
# attribute we might consider the following solution:
# """
#
#
# c_ GeometricRectangle
#     ___ - width_0 height_0
#         ?  ?
#         ?  ?
#
#     ___ area
#         r_ ? * ?
#
#
# shape = G... 2 5
#
#
# ___ name
#     r_ "I'm a rectangle"
#
#
# shape.name = name()
# print(shape.name)  # Prints: I’m a rectangle
