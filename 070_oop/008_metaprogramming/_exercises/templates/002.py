# # Abstract base classes (ABCs) enforce what derived classes implement particular methods from the base class.
# #
# # To understand how this works and why we should use it, let's take a look at an example that Van Rossum would enjoy.
# # Let's say we have a Base class "MontyPython" with two methods (joke & punchline) that must be implemented by all derived classes.
#
#
# c_ MontyPython
#     ___ joke
#         r_ N...
#
#     ___ punchline
#         r_ N..
#
#
# c_ ArgumentClinic ?
#     ___ joke
#         r_ "Hahahahahah"
#
# # When we instantiate an object and call it's two methods, we'll get an error (as expected) with the punchline() method.
#
#
# sketch = A..
# ?.p..
#
#
# # NotImplementedError
# # However, this still allows us to instantiate an object of the ArgumentClinic class without getting an error.
# # In fact we don't get an error until we look for the punchline().
# # This is avoided by using the Abstract Base Class (ABC) module. Let's see how this works with the same example:
#
# ____ a.. _______ A.. a..
#
#
# c_ MontyPython m..
#     ??
#     ___ joke
#         p..
#
#
# ??
# ___ punchline
#     p..
#
#
# c_ ArgumentClinic M..
#     ___ joke
#         r_ "Hahahahahah"
#
#
# # This time when we try to instantiate an object from the incomplete class, we immediately get a TypeError!
#
# c = A..
#
# # TypeError:
# # "Can't instantiate abstract class ArgumentClinic with abstract methods punchline"
# # In this case, it's easy to complete the class to avoid any TypeErrors:
#
# c_ ArgumentClinic M..
#     ___ joke
#         r_ "Hahahahahah"
#
#     ___ punchline
#         r_ "Send in the constable!"
#
# # This time when you instantiate an object it works!
