# # As you can see, multiple inheritance can be useful but also lead to very complicated situations and code that
# # is hard to read. It's also rare to have objects that neatly inherit everything from more than multiple other objects.
# #
# # If you see yourself beginning to use multiple inheritance and a complicated class hierarchy,
# # it's worth asking yourself if you can achieve code that is cleaner and easier to understand by using composition
# # instead of inheritance. Since this article is focused on inheritance, I won't go into too much detail
# # on composition and how to wield it in Python. Luckily, Real Python has published a deep-dive guide
# # to both inheritance and composition in Python that will make you an OOP pro in no time.
# #
# # There's another technique that can help you get around the complexity of multiple inheritance while still
# # providing many of the benefits. This technique is in the form of a specialized, simple class called a mixin.
# #
# # A mixin works as a kind of inheritance, but instead of defining an "is-a" relationship it may be more accurate
# # to say that it defines an "includes-a" relationship. With a mix-in you can write a behavior that can be directly
# # included in any number of other classes.
# #
# # Below, you will see a short example using VolumeMixin to give specific functionality to our 3D objects-in this case,
# # a volume calculation:
#
# c_ Rectangle:
#     ___  -  length, width):
#         length _ length
#         width _ width
#
#     ___ area
#         r_ length * width
#
# c_ Square(Rectangle):
#     ___  -  length):
#         s__ . - (length, length)
#
# c_ VolumeMixin:
#     ___ volume
#         r_ area() * height
#
# c_ Cube(VolumeMixin, Square):
#     ___  -  length):
#         s__ . - (length)
#         height _ length
#
#     ___ face_area
#         r_ s__ .area()
#
#     ___ surface_area
#         r_ s__ .area() * 6
#
# # In this example, the code was reworked to include a mixin called VolumeMixin. The mixin is then used by Cube
# # and gives Cube the ability to calculate its volume, which is shown below:
# #
# cube _ Cube(2)
# cube.surface_area()
# # 24
#
# cube.volume()
# # 8
#
# # This mixin can be used the same way in any other class that has an area defined for it and for which
# # the formula area * height returns the correct volume.
# # A super() Recap
# # In this tutorial, you learned how to supercharge your classes with super(). Your journey started with
# # a review of single inheritance and then showed how to call superclass methods easily with super().
# # You then learned how multiple inheritance works in Python, and techniques to combine super()
# # with multiple inheritance. You also learned about how Python resolves method calls using the method resolution
# # order (MRO), as well as how to inspect and modify the MRO to ensure appropriate methods are called
# # at appropriate times.
# # For more information about object-oriented programming in Python and using super(), check out these resources:
