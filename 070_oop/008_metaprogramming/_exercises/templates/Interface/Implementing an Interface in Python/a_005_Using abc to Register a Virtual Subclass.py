# # Using abc to Register a Virtual Subclass
# # Once you've imported the abc module, you can directly register a virtual subclass by using the .register() metamethod.
# # In the next example, you register the interface Double as a virtual base class of the built-in __float__ class:
#
# c_ Double m..
#     """Double precision floating point number."""
#     pass
#
# ?.re.. fl..
#
# # You can check out the effect of using .register():
#
# iss.. fl.. D..
# # True
#
# isi.. 1.2345 D..
# # True
#
# # By using the .register() meta method, you've successfully registered Double as a virtual subclass of float.
# # Once you've registered Double, you can use it as class decorator to set the decorated class as a virtual subclass:
#
# ??.re..
# c_ Double64
#     """A 64-bit double-precision floating-point number."""
#     p..
#
# print(iss.. D_64 D..  # True
#
# # The decorator register method helps you to create a hierarchy of custom virtual class inheritance.
