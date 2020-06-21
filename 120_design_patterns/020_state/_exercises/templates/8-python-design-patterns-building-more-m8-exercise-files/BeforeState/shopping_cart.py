# # Define the states
#
# EMPTY _ 0
# N.. _ 1
# AT_CHECKOUT _ 2
# PAID_FOR _ 3
#
# c_ ShoppingCart
#
#     ___ -
#         state _ E...
#         _i.. _ 0
#
#     ___ add_item
#         __ st.. __ E..
#             print('You added the first item')
#             st.. _ N..
#             _i.. +_ 1
#
#         ____ st.. __ N..
#             _i.. +_ 1
#             print('You now have @ items in your cart'.f.. _i..
#
#         ____ st.. __ AT_CHECKOUT:
#             print("You can't add new items at checkout!")
#
#         ____ # state __ PAID_FOR
#             print("You can't add items after payment!")
#
#     ___ remove_item
#         __ st.. __ E..
#             print('Your cart is empty! Nothing to remove!!')
#
#         ____ st.. __ N..
#             _i.. -_ 1
#             print('You now have @ items in your cart'.f.. _i..
#             __ no. _i..:
#                 st.. _ E..
#
#         ____ st.. __ A...
#             _i.. -_ 1
#             print('You now have @ items in your cart'.f.. _i..
#             __ no. _i..
#                 st.. _ E..
#             ____
#                 st.. _ N..
#
#         ____ # state __ PAID_FOR
#             print("You can't add items after payment!")
#
#     ___ checkout
#         __ st.. __ E..
#             print("Your cart is empty. Go shopping!")
#
#         ____ st.. __ N..
#             print('You now have @ items in your cart'.f.. _i..
#             st.. _ A...
#
#         ____ st.. __ A..
#             print('You are already at check out!')
#
#         ____ # state __ PAID_FOR
#             print("You can't go back to checkout after payment.")
#
#     ___ paid_for
#         __ st.. __ E..
#             print("Your cart is empty. How did you get here?")
#
#         ____ st.. __ N..
#             print("You must go to checkout for payment.")
#
#         ____ st.. __ A..
#             print('You paid for @ items.'.f.. _i..
#             _i.. _ 0
#             st.. _ E..
#
#         ____ # state __ PAID_FOR
#             print("You already paid for your purchases.")
