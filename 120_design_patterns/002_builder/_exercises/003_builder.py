# """Builder pattern
#
# The Builder pattern separates the construction of a complex object from its
# representation so that the same construction process can create different
# representations.
# """
# ____ a.. _____ A.. a..
#
#
# c_ IceCream A..
#     """Abstract Product."""
#
#     ??
#     ___ need_spoon ____
#         r_ F..
#
#     ___ -s ____
#         string = ____. -c . -n
#         ___ key value __ ____. -d.i..
#             s.. += "\n@: @".f.. ? ?
#         s... += "\n"
#         r_ s...
#
#
# c_ ConeIceCream IC..
#     """Concrete Product 1."""
#     pass
#
#
# c_ CupIceCream IC..
#     """Concrete Product 2."""
#
#     ??
#     ___ need_spoon ____
#         r_ T..
#
#
# c_ Builder A..
#     """Specify the abstract interface that creates all parts of the product.
#
#     This Abstract interface is used by a Director object. All methods except
#     "get_product" return self, so this class is a "fluent interface".
#     """
#
#     @??
#     ___ - ____
#         ____.product = N..
#         ____.toppings = N..
#
#     ___ set_flavors ____ flavors
#         ____.p__.? _ ?
#         r_ ____
#
#     ___ set_toppings ____
#         __ ____.t... __ no. N..
#             ____.p___.t.. _ ____.?
#         r_ ____
#
#     ___ add_spoon ____
#         __ ____.p__.need_spoon
#             ____.p___.spoon = 1
#         r_ ____
#
#     ___ get_product ____
#         r_ ____.p..
#
#
# c_ ConeIceCreamBuilder B..
#     """Concrete Builder 1.
#
#     This class assembles the product by implementing the Builder interface.
#     It defines and keeps track of the representation it creates.
#     """
#
#     ___ - ____
#         # super().__init__()  # ok in Python 3.x, not in 2.x
#         s.. ____. -c ____ |. -  # also ok in Python 2.x
#         ____.product _ CIC..
#         ____.toppings _ "hazelnuts"
#
#
# c_ CupIceCreamBuilder B..
#     """Concrete Builder 2.
#
#     This class assembles the product by implementing the Builder interface.
#     It defines and keeps track of the representation it creates.
#     """
#
#     ___ - ____
#         # super().__init__()  # ok in Python 3.x, not in 2.x
#         s.. ____. -c  ____|. -  # also ok in Python 2.x
#         ____.product _ CIC..
#         ____.toppings _ "chocolate chips"
#
#
# c_ Director o..
#     """Build an object using the Builder interface."""
#
#     ___ - ____ builder
#         ____.? _ ?
#
#     ___ build_product ____ flavors
#         """Prepare the product and finally return it to the client.
#
#         The Builder class defined above is a "fluent interface", so we can use
#         method chaining.
#
#         Parameters
#         ----------
#         flavors : list
#
#         Returns
#         -------
#         ConeIceCream or CupIceCream
#         """
#         r_ ____.b__.set_flavors(
#             f..
#         ).s_t__.ad__.g_p..
#
#
# # Client: it creates a Director object and configures it with a Builder object.
#
#
# ___ main
#     director = D.. CICB..
#     product = ?.b_p.. "chocolate", "vanilla", "banana"
#     print ?
#
#     director = D.. CICB..
#     product = ?.b_p.. "lemon", "strawberry"
#     print ?
#
#     builder = CICB..
#     director = D.. ?
#     b__.t.. _ N..  # the ConeIceCreamBuilder has no more toppings!
#     product _ d__.b.. "chocolate", "vanilla", "banana"
#     print ?
#
#
# __ _______ __ ______
#     main
