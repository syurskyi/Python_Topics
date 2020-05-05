# # Inheritance is the concept in object-oriented programming in which a class derives (or inherits) attributes
# # and behaviors from another class without needing to implement them again.
#
# # See the following program.
#
# # app.py
#
# c_ Rectangle
#     __ - length width
#         ?  ?
#         ?  ?
#
#     __ area
#         r_ ? * ?
#
#     __ perimeter
#         r_ 2 * l.. + 2 * w..
#
#
# c_ Square
#     __ - length
#         ?  ?
#
#     __ area
#         r_ l.. * l..
#
#     __ perimeter
#         r_ 4 * l..
#
#
# sqr _ S.. 4
# print("Area of Square is:", ?.a..
#
# rect _ R.. 2 4
#
# # See the output.
# #
# #   pyt python3 app.py
# # Area of Square is: 16
# # Area of Rectangle is: 8
# #   pyt
#
# # In the above example, you have two shapes that are related to each other: The square is, which is the particular
# # kind of rectangle.
# #
# # The code, however, doesn't reflect the relationship between those two shapes and thus has code that is necessarily
# # repeated. We need to apply basic code principles like Do not repeat yourself.
# #
# # By using the proper way of inheritance, you can reduce the amount of code you write while simultaneously
# # reflecting the real-world relationship between those shapes like rectangles and squares.
#
# # app.py
#
# c_ Rectangle
#     __ - lengt width
#         ?  ?
#         ?  ?
#
#     __ area
#         r_ ? * ?
#
#     __ perimeter
#         r_ 2 * ? + 2 * ?
#
# c_ Square R..
#     __ - length
#         s__. - l.. l..
#
#
# sqr _ S.. 4
# print("Area of Square is:" ?.a..
#
# rect _ R. 2 4
# print("Area of Rectangle is:" ?.a..
#
# # In this example, a Rectangle is a superclass, and Square is a subclass because the Square and Rectangle __init__()
# # methods are so related, we can call a superclass's __init__() method (Rectangle.__init__()) from that of Square
# # by using a super() keyword.
# #
# # This sets the length and width attributes even though you just had to supply the single length parameter to a Square constructor.
# #
# # When you run this, even though your Square class doesn't explicitly implement it, the call to .area() will use
# # an area() method in the superclass and print 16.
# #
# # The Square class inherited .area() from the Rectangle class.
# #
# # See the output.
# #
# #   pyt python3 app.py
# # Area of Square is: 16
# # Area of Rectangle is: 8
# #  pyt
# # It is the same as above.
#
