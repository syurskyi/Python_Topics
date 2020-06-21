# # The method resolution order (or MRO) tells Python how to search for inherited methods.
# # This comes in handy when you're using super() because the MRO tells you exactly where Python will look for
# # a method you're calling with super() and in what order.
# #
# # Every class has an .__mro__ attribute that allows us to inspect the order, so let;s do that:
#
# RightPyramid.__mro__
# # (<class '__main__.RightPyramid'>, <class '__main__.Triangle'>,
# #  <class '__main__.Square'>, <class '__main__.Rectangle'>,
# #  <class 'object'>)
#
# # This tells us that methods will be searched first in Rightpyramid, then in Triangle, then in Square, then Rectangle,
# # and then, if nothing is found, in object, from which all classes originate.
# # The problem here is that the interpreter is searching for .area() in Triangle before Square and Rectangle,
# # and upon finding .area() in Triangle, Python calls it instead of the one you want. Because Triangle.area()
# # expects there to be a .height and a .base attribute, Python throws an AttributeError.
# # Luckily, you have some control over how the MRO is constructed. Just by changing the signature
# # of the RightPyramid class, you can search in the order you want, and the methods will resolve correctly:
#
# c_ RightPyramid(Square, Triangle):
#     ___  -  base, slant_height):
#         base _ base
#         slant_height _ slant_height
#         s__ . - (base)
#
#     ___ area
#         base_area _ s__ .area()
#         perimeter _ s__ .perimeter()
#         r_ 0.5 * perimeter * slant_height + base_area
#
#
# # Notice that RightPyramid initializes partially with the .__init__() from the Square class.
# # This allows .area() to use the .length on the object, as is designed.
# #
# # Now, you can build a pyramid, inspect the MRO, and calculate the surface area:
# #
# pyramid _ RightPyramid(2, 4)
# RightPyramid.__mro__
# # (<class '__main__.RightPyramid'>, <class '__main__.Square'>,
# # <class '__main__.Rectangle'>, <class '__main__.Triangle'>,
# # <class 'object'>)
#
# pyramid.area()
# # 20.0
#
# # You see that the MRO is now what you'd expect, and you can inspect the area of the pyramid as well, thanks
# # to .area() and .perimeter().
# #
# # There's still a problem here, though. For the sake of simplicity, I did a few things wrong in this example:
# # the first, and arguably most importantly, was that I had two separate classes with the same method name and signature.
# # This causes issues with method resolution, because the first instance of .area() that is encountered
# # in the MRO list will be called.
# #
# # When you're using super() with multiple inheritance, it's imperative to design your classes to cooperate.
# # Part of this is ensuring that your methods are unique so that they get resolved in the MRO, by making sure
# # method signatures are unique-whether by using method names or method parameters.
# #
# # In this case, to avoid a complete overhaul of your code, you can rename the Triangle class's .area() method
# # to .tri_area(). This way, the area methods can continue using class properties rather than taking external parameters:
#
# c_ Triangle:
#     ___  -  base, height):
#         base _ base
#         height _ height
#         s__ . - ()
#
#     ___ tri_area
#         r_ 0.5 * base * height
#
# # Let's also go ahead and use this in the RightPyramid class:
#
# c_ RightPyramid(Square, Triangle):
#     ___  -  base, slant_height):
#         base _ base
#         slant_height _ slant_height
#         s__ . - (base)
#
#     ___ area
#         base_area _ s__ .area()
#         perimeter _ s__ .perimeter()
#         r_ 0.5 * perimeter * slant_height + base_area
#
#     ___ area_2
#         base_area _ s__ .area()
#         triangle_area _ s__ .tri_area()
#         r_ triangle_area * 4 + base_area
#
#
# # The next issue here is that the code doesn't have a delegated Triangle object like it does for a Square object,
# # so calling .area_2() will give us an AttributeError since .base and .height don't have any values.
# #
# # You need to do two things to fix this:
# #
# # All methods that are called with super() need to have a call to their superclass's version of that method.
# # This means that you will need to add super().__init__() to the .__init__() methods of Triangle and Rectangle.
# #
# # Redesign all the .__init__() calls to take a keyword dictionary. See the complete code below.
#
# c_ Rectangle:
#     ___  -  length, width, **kwargs):
#         length _ length
#         width _ width
#         s__ . - (**kwargs)
#
#     ___ area
#         r_ length * width
#
#     ___ perimeter
#         r_ 2 * length + 2 * width
#
# # Here we declare that the Square class inherits from
# # the Rectangle class
#
# c_ Square(Rectangle):
#     ___  -  length, **kwargs):
#         s__ . - (length_length, width_length, **kwargs)
#
# c_ Cube(Square):
#     ___ surface_area
#         face_area _ s__ .area()
#         r_ face_area * 6
#
#     ___ volume
#         face_area _ s__ .area()
#         r_ face_area * length
#
# c_ Triangle:
#     ___  -  base, height, **kwargs):
#         base _ base
#         height _ height
#         s__ . - (**kwargs)
#
#     ___ tri_area
#         r_ 0.5 * base * height
#
# c_ RightPyramid(Square, Triangle):
#     ___  -  base, slant_height, **kwargs):
#         base _ base
#         slant_height _ slant_height
#         kwargs["height"] _ slant_height
#         kwargs["length"] _ base
#         s__ . - (base_base, **kwargs)
#
#     ___ area
#         base_area _ s__ .area()
#         perimeter _ s__ .perimeter()
#         r_ 0.5 * perimeter * slant_height + base_area
#
#     ___ area_2
#         base_area _ s__ .area()
#         triangle_area _ s__ .tri_area()
#         r_ triangle_area * 4 + base_area
#
# # There are a number of important differences in this code:
# # kwargs is modified in some places (such as RightPyramid.__init__()): This will allow users of these objects
# # to instantiate them only with the arguments that make sense for that particular object.
# # Setting up named arguments before **kwargs: You can see this in RightPyramid.__init__().
# # This has the neat effect of popping that key right out of the **kwargs dictionary, so that by the time that
# # it ends up at the end of the MRO in the object class, **kwargs is empty.
#
# # Now, when you use these updated classes, you have this:
# #
# pyramid _ RightPyramid(base_2, slant_height_4)
# pyramid.area()
# # 20.0
# pyramid.area_2()
#
# # 20.0
# # It works! You've used super() to successfully navigate a complicated class hierarchy while using both inheritance
# # and composition to create new classes with minimal reimplementation.
#
#
#
