# # Example of unwrapping a decorator
#
# ____ fun.. ______ w...
#
# ___ decorator1 func
#     ?w.. ?
#     ___ wrapper $ $$
#         print('Decorator 1')
#         r_ ? $ $$
#     r_ ?
#
# ___ decorator2 func
#     ?w.. ?
#     ___ wrapper $ $$
#         print('Decorator 2')
#         r_ ? $ $$
#     r_ ?
#
# ?_1
# ?_2
# ___ add x, y
#     r_ ? + ?
#
# # Calling wrapped function
# print(? 2,3
#
# # Calling original function
# print ?. -w 2,3
#
#
# # Problem
# # A decorator has been applied to a function, but you want to “undo” it, gaining access to
# # the original unwrapped function.
# # Solution
# # Assuming that the decorator has been implemented properly using @wraps (see
# # Recipe 9.2), you can usually gain access to the original function by accessing the __wrap
# # ped__ attribute. For example:
#
# # Discussion
# # Gaining direct access to the unwrapped function behind a decorator can be useful for
# # debugging, introspection, and other operations involving functions. However, this
# # recipe only works if the implementation of a decorator properly copies metadata using
# # @wraps ____ the functools module or sets the __wrapped__ attribute directly.
# # If multiple decorators have been applied to a function, the behavior of accessing __wrap
# # ped__ is currently undefined and should probably be avoided. In Python 3.3, it bypasses
# # all of the layers. For example, suppose you have code like this:
#
# # However, this behavior has been reported as a bug (see http://bugs.python.org/
# # issue17482) and may be changed to explose the proper decorator chain in a future release.
# # Last, but not least, be aware that not all decorators utilize @wraps, and thus, they may
# # not work as described. In particular, the built-in decorators @staticmethod and @class
# # method create descriptor objects that don’t follow this convention (instead, they store
# # the original function in a __func__ attribute). Your mileage may vary.
