# """
# Separate the construction of a complex object from its representation so
# that the same construction process can create different representations.
# """
#
# _______ a..
#
#
# c_ Director
#     """
#     Construct an object using the Builder interface.
#     """
#
#     ___ -
#         _builder = N..
#
#     ___ construct builder
#         _?  ?
#         _b__._b_a
#         _b__._b_b
#         _b__._b_c
#
#
# c_ Builder m..
#     """
#     Specify an abstract interface for creating parts of a Product
#     object.
#     """
#
#     ___ -
#         self.product = Product()
#
#     ??.?
#     ___ _build_part_a
#         p..
#
#     ??.?
#     ___ _build_part_b
#         p..
#
#     ??.?
#     ___ _build_part_c
#         p..
#
#
# c_ ConcreteBuilder B..
#     """
#     Construct and assemble parts of the product by implementing the
#     Builder interface.
#     Define and keep track of the representation it creates.
#     Provide an interface for retrieving the product.
#     """
#
#     ___ _build_part_a
#         p..
#
#     ___ _build_part_b
#         p..
#
#     ___ _build_part_c
#         p..
#
#
# c_ Product
#     """
#     Represent the complex object under construction.
#     """
#
#     p..
#
#
# ___ main
#     concrete_builder = C..
#     director = D..
#     ?.c.. ?
#     product = c__.pr..
#
#
# __ _______ __ ______
#     ?
