# # If you're unfamiliar with object-oriented programming concepts, inheritance might be an unfamiliar term.
# # Inheritance is a concept in object-oriented programming in which a class derives (or inherits) attributes
# # and behaviors from another class without needing to implement them again.
# #
# # For me at least, it's easier to understand these concepts when looking at code, so let's write classes describing
# # some shapes:
#
# c_ Rectangle
#     ___ -  length width
#         ? ?
#         ? ?
#
#     ___ area
#         r_ ? * ?
#
#     ___ perimeter
#         r_ 2 * ? + 2 * ?
#
# c_ Square:
#     ___ - length
#         ? ?
#
#     ___ area
#         r_ l.. * l..
#
#     ___ perimeter
#         r_ 4 * l..
#
# square _ S.. 4
# ?.a..
# # 16
#
# rectangle _ R.. 24
# ?.a..
# # 8
#
# # In this example, you have two shapes that are related to each other: a square is a special kind of rectangle.
# # The code, however, doesn't reflect that relationship and thus has code that is essentially repeated.
# #
# # By using inheritance, you can reduce the amount of code you write while simultaneously reflecting the real-world
# # relationship between rectangles and squares:
#
# c_ Rectangle
#     ___ - length width
#         ? ?
#         ? ?
#
#     ___ area
#         r_ ? * ?
#
#     ___ perimeter
#         r_ 2 * ? + 2 * ?
#
# # Here we declare that the Square class inherits from the Rectangle class
# c_ Square R..
#     ___ - length
#         s__. - l.. l..
#
# # Here, you've used super() to call the __init__() of the Rectangle class, allowing you to use it in the Square class
# # without repeating code. Below, the core functionality remains after making changes:
#
# square _ S.. 4
# ?.a..
# # 16
#
#
# # In this example, Rectangle is the superclass, and Square is the subclass.
# #
# # Because the Square and Rectangle .__init__() methods are so similar, you can simply call the superclass's
# # .__init__() method (Rectangle.__init__()) from that of Square by using super(). This sets the .length and .width
# # attributes even though you just had to supply a single length parameter to the Square constructor.
# #
# # When you run this, even though your Square class doesn't explicitly implement it, the call to .area() will
# # use the .area() method in the superclass and print 16. The Square class inherited .area() from the Rectangle class.
#
