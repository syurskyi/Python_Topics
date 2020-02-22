# """
# Provide an interface for creating families of related or dependent
# objects without specifying their concrete classes.
# """
#
# ______ a..
#
#
# c_ AbstractFactory m..
#     """
#     Declare an interface for operations that create abstract product
#     objects.
#     """
#
#     ??.?
#     ___ create_product_a
#         p..
#
#     ??.?
#     ___ create_product_b
#         p..
#
#
# c_ ConcreteFactory1 A..
#     """
#     Implement the operations to create concrete product objects.
#     """
#
#     ___ create_product_a
#         r_ C_A1
#
#     ___ create_product_b
#         r_ C_B1
#
#
# c_ ConcreteFactory2 A..
#     """
#     Implement the operations to create concrete product objects.
#     """
#
#     ___ create_product_a
#         r_ C_A2
#
#     ___ create_product_b
#         r_ C_B2
#
#
# c_ AbstractProductA m..
#     """
#     Declare an interface for a type of product object.
#     """
#
#     ??.?
#     ___ interface_a
#         p..
#
#
# c_ ConcreteProductA1 A_A
#     """
#     Define a product object to be created by the corresponding concrete
#     factory.
#     Implement the AbstractProduct interface.
#     """
#
#     ___ interface_a
#         p..
#
#
# c_ ConcreteProductA2 A_A
#     """
#     Define a product object to be created by the corresponding concrete
#     factory.
#     Implement the AbstractProduct interface.
#     """
#
#     ___ interface_a
#         p..
#
#
# c_ AbstractProductB m..
#     """
#     Declare an interface for a type of product object.
#     """
#
#     ??.?
#     ___ interface_b
#         p..
#
#
# c_ ConcreteProductB1 A_B
#     """
#     Define a product object to be created by the corresponding concrete
#     factory.
#     Implement the AbstractProduct interface.
#     """
#
#     ___ interface_b
#         p..
#
#
# c_ ConcreteProductB2 A_B
#     """
#     Define a product object to be created by the corresponding concrete
#     factory.
#     Implement the AbstractProduct interface.
#     """
#
#     ___ interface_b
#         p..
#
#
# ___ main
#     ___ factory __ C_1 C_2
#         product_a = ?.c_a
#         product_b = ?.c_b
#         pr_a.i_a
#         pr_b.i_b
#
#
# __ _______ __ _____
#     ?