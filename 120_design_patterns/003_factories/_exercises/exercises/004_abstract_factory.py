# # coding: utf-8
#
#
# c_ AbstractFactory o..
#     ___ create_drink
#         r_ N...
#
#
#     ___ create_food
#         r_ N...
#
#
# c_ Drink o..
#     ___ -  name
#         _?  ?
#
#     ___ -s
#         r_ _n..
#
#
# c_ Food o..
#     ___ - name
#
#         _?  ?
#
#
#     ___ -s
#         r_ _n..
#
#
# c_ ConcreteFactory1 A..
#     ___ create_drink
#         r_ D.. 'Coca-cola'
#
#
#     ___ create_food
#         r_ F.. 'Hamburger'
#
#
# c_ ConcreteFactory2 A..
#     ___ create_drink
#         r_ D.. 'Pepsi'
#
#     ___ create_food
#         r_ F.. 'Cheeseburger'
#
#
# ___ get_factory ident
#     __ ? __ 0
#         r_ C_1
#     ____ ident __ 1
#         r_ C_2
#
# factory = g.. 1
# print(?.c_d..  # Pepsi
# print(?.c_f..  # Cheeseburger