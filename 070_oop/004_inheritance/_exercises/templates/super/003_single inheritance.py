# # Prerequisites: Inheritance, function overriding
# #
# # At a fairly abstract level, super() provides the access to those methods of the super-class (parent class)
# # which have been overridden in a sub-class (child class) that inherits from it. Consider
# # the code example given below, here we have a class named Square and an another class named Cube which inherits
# # the class Square.
#
# c_ Square:
#      ___  -  side
#          ? ?
#
#      ___ area
#          r_ ? * ?
#
# c_ Cube S..
#     ___ area
#         face_area _ side * side
#         r_ face_area * 6
#
#     ___ volume
#         face_area _ side * side
#         r_ face_area * side
#
# # Note: Since Cube class does not have an __init__() method, the __init__() of Square class will be used for
# # initialization of Cube instances (basic property of inheritance).
#
# # Considering this example, we know that each face of a cube is a square and hence, face_area of
# # Cube represents area of a Square. Now, it makes sense to evaluate face_area using area() method of
# # the class Square rather than calculating it manually, not only this will save us from rewriting the code but also
# # it will allow to change the area() logic from one place. But as we have overridden the area() method in Cube,
# # we cannot call area() method of Square using self.area().
# # Now, this is a situation where super() comes in rescue. super() returns a proxy object of the parent class and
# # then you call the method of your choice on that proxy object, thus, we can call the area() method of
# # Square class using super() as, super().area(). Here follows a modified definition of the class Cube.
#
# c_ Cube S00..
#      ___ area
#          r_ s__ .a.. * 6
#
#      ___ volume
#          r_ s__ .a.. * s..
#
#
# # Note that we could have called the area() of Square method as Square.area() rather than super().area()
# # but the latter maker is easier to swap out the super-class or rename it when required, making the code much
# # easier to maintain.
# #
# # Passing arguments in super()
# # In the previous section, we discussed how to use super() without any parameters, but that only provides us
# # access to the methods of that super-class which is the immediate parent of the sub-class.
# #
# # To access the methods of that super-class which is not an immediate parent of the sub-class, we use super()
# # with two arguments. Let's consider an example of three classes named Square, SquarePrism and Cube
# # to understand how to use super() with arguments.
# # Now, a cube is just a special type of square prism whose height is equal to the side of it's base, and hence
# # a Cube resembles a SquarePrism much more than it resembles a Square. Therefore, in this example
# # the class Cube will inherit the class SquarePrism, and the class
# # SquarePrism will inherit the class Square. For class Square we'll use the same definition we used in
# # the previous section. Given below is the definition of our newly defined class, SquarePrism.
# #
#
# c_ SquarePrism S..
#      ___  -  side height
#          ? ?
#          ? ?
#
#      ___ face_area
#          base_area _ s__ .a..
#          lateral_area _ s.. * h..
#          r_ b.. l..
#
#      ___ area
#          base_area _ s__ .a..
#          lateral_area _ s.. * h..
#          r_ 2 * base_area + 4 * lateral_area
#
# # A SquarePrism instance has two attributes, the side of it's square base and the height of the square prism.
# # The instance method face_area() returns a tuple of two numbers representing the base area of the square prism and
# # the lateral area of the square prism. Since the base is a square, for base area of the square prism,
# # we call the method Square.area() as super().area(). The area() method returns the total surface area of
# # the square prism.
# #
# # Until now, we have used super() without any parameters, now follows the definition of
# # the new class Cube which will demonstrate the use of super() with parameters.
# #
# c_ Cube SP..
#      ___  -  side
#          s__ . - side _ ? height _ s..
#
#      ___ face_area
#          r_ s__ SP.. ? .a..
#
#      ___ area
#          r_ s__ .a..
#
# # Unlike the methods __init__() and area(), the face_area() method of Cube is somewhat different from its
# # counter-part SquarePrism.face_area(). For a cube the lateral area is equal to the base area and hence,
# # it is not meaningful for the face_area() method to return a tuple, therefore, the face_area()
# # of the class Cube will return the area of one of the cube faces.
# # Now, since each face of the cube is a square, it is again meaningful to use the area() method of the class Square.
# # Now, since the class Square is not an immediate parent of the class Cube, we cannot access the area() method
# # of the class Square as super().area() as it will call the method SquarePrism.area() instead.
# #
# # Here we use super(SquarePrism, self).face_area() to call the area() method of the class Square.
# # In the first argument, SquarePrism signifies that super() searches for the area() method in the immediate parent
# # of the class SquarePrism, that is in the class Square. The use of self as the second parameter provides
# # the context of the current Cube object to super() for the requested area() method to act upon.
# # Remember that, to use super() in two argument form, it is necessary that the object passed as the second argument
# # is an instance of the type passed as first argument.
# # Note: Since the class Cube is a child of the class SquarePrism, a Cube instance is also an instance
# # of the class SquarePrism and the class Square
# # Try the following code snippet and observe the output for the clarification of the above point.
# #
#
# c_ Square
#     ___  -
#         p..
#
# c_ SquarePrism S..
#     ___  -
#         p..
#
# c_ Cube SP..
#     ___  -
#         p..
#
# square _ S..
# squareprism _ SP..
# cube _ C..
#
# print(isi.. sp.. S..
# print(isi.. c.. S..
#
# # It is worthwhile to note that the zero argument form of super() can only be used inside a class definition
# # as it is auto-filled by the compiler with the appropriate parameters, i.e. if we use super() inside a class, say X,
# # super() will be converted into super(X, self) by the compiler.
# #
# # While the zero-argument form of super() is popular among developers the two argument form might not seem
# # to be of much use for now. But in multiple inheritance, the two argument form plays a very important role.
#
