# # Before heading into multiple inheritance, let's take a quick detour into the mechanics of super().
# #
# # While the examples above (and below) call super() without any parameters, super() can also take two parameters:
# # the first is the subclass, and the second parameter is an object that is an instance of that subclass.
# #
# # First, let's see two examples showing what manipulating the first variable can do, using the classes already shown:
#
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
#
# c_ Square R..
#     ___ - length
#         s____ ? ?. - l.. l...
#
# # In Python 3, the super(Square, self) call is equivalent to the parameterless super() call. The first parameter
# # refers to the subclass Square, while the second parameter refers to a Square object which, in this case, is self.
# # You can call super() with other classes as well:
#
#
# c_ Cube S..
#     ___ surface_area
#         face_area _ s__ ? ?.a..
#         r_ ? * 6
#
#     ___ volume
#         face_area _ s___ ? ?.a..
#         r_ ? * l..
#
#
# # In this example, you are setting Square as the subclass argument to super(), instead of Cube. This causes super()
# # to start searching for a matching method (in this case, .area()) at one level above Square in the instance hierarchy,
# # in this case Rectangle.
# #
# # In this specific example, the behavior doesn't change. But imagine that Square also implemented an .area() function
# # that you wanted to make sure Cube did not use. Calling super() in this way allows you to do that.
# #
# # Caution: While we are doing a lot of fiddling with the parameters to super() in order to explore how it works
# # under the hood, I'd caution against doing this regularly.
# #
# # The parameterless call to super() is recommended and sufficient for most use cases, and needing to change
# # the search hierarchy regularly could be indicative of a larger design issue.
# #
# # What about the second parameter? Remember, this is an object that is an instance of the c_ used as
# # the first parameter. For an example, isinstance(Cube, Square) must return True.
# #
# # By including an instantiated object, super() returns a bound method: a method that is bound to the object,
# # which gives the method the object's context such as any instance attributes. If this parameter is not included,
# # the method returned is just a function, unassociated with an object's context.
# #
# # For more information about bound methods, unbound methods, and functions, read the Python documentation
# # on its descriptor system.
# #
# # Note: Technically, super() doesn't return a method. It returns a proxy object. This is an object that
# # delegates calls to the correct c_ methods without making an additional object in order to do so.
#
