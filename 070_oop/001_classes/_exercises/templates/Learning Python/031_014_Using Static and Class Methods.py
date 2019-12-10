# c_ Methods
#     __ imeth ____  x            # Normal instance method: passed a ____
#         print ____ x
#
#     __ smeth x                  # Static: no instance passed
#         print(x)
#
#     __ cmeth ___ x             # Class: gets class, not instance
#         print ___ x
#
#     smeth = st... sm..    # Make smeth a static method
#     cmeth = cl... cm..     # Make cmeth a class method
#
#
#
# obj = ?                # Make an instance
#
# ?.im.. 1                   # Normal method, call through instance
# # <__main__.Methods object...> 1     # Becomes imeth(obj, 1)
#
# M_.im__ ob. 2          # Normal method, call through class
# # <__main__.Methods object...> 2     # Instance passed explicitly
#
# M_.sm.. 3               # Static method, call through class
#                                   # No instance passed or expected
#
# o__.sm.. 4                   # Static method, call through instance
#                                   # Instance not passed
#
# M__.cm.. 5               # Class method, call through class
# # <class '__main__.Methods'> 5       # Becomes cmeth(Methods, 5)
#
# o_.cm.. 6                   # Class method, call through instance
# # <class '__main__.Methods'> 6       # Becomes cmeth(Methods, 6)
