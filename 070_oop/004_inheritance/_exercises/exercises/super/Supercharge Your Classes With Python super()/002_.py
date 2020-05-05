# # So what can super() do for you in single inheritance?
# # Like in other object-oriented languages, it allows you to call methods of the superclass in your subclass.
# # The primary use case of this is to extend the functionality of the inherited method.
# # In the example below, you will create a class Cube that inherits from Square and extends the functionality
# # of .area() (inherited from the Rectangle class through Square) to calculate the surface area and volume of
# # a Cube instance:
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
# c_ Square R..
#     ___ - length
#         s___. - l.. l..
#
# c_ Cube S..
#     ___ surface_area(
#         face_area _ s__.a..
#         r_ ? * 6
#
#     ___ volume
#         f_a.. _ s__.a..
#         r_ f_a * l..
#
#
# # Now that you've built the classes, let's look at the surface area and volume of a cube with a side length of 3:
#
# cube = C.. 3
# ?.s_a..
# # 54
#
# ?.v..
# # 27
#
#
# # Caution: Note that in our example above, super() alone won't make the method calls for you: you have to call
# # the method on the proxy object itself. Here you have implemented two methods for the Cube class:
# # .surface_area() and .volume(). Both of these calculations rely on calculating the area of a single face,
# # so rather than reimplementing the area calculation, you use super() to extend the area calculation.
# #
# # Also notice that the Cube class definition does not have an .__init__(). Because Cube inherits from Square and
# # .__init__() doesn't really do anything differently for Cube than it already does for Square,
# # you can skip defining it, and the .__init__() of the superclass (Square) will be called automatically.
# #
# # super() returns a delegate object to a parent class, so you call the method you want directly on it: super().area().
# #
# # Not only does this save us from having to rewrite the area calculations, but it also allows us to change
# # the internal .area() logic in a single location. This is especially in handy when you have a number
# # of subclasses inheriting from one superclass.
#
#
