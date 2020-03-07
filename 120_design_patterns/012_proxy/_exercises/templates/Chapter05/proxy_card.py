# ____ a.. ______ A.. a..
#
# c_ Payment m..
#
#     ??
#     ___ do_pay
#         p..
#
# c_ Bank P..
#
#     ___ -
#         card _ N..
#         account _ N..
#
#     ___ __getAccount
#         account _ card # Assume card number is account number
#         r_ ?
#
#     ___ __hasFunds
#         print("Bank:: Checking if Account", __gA.., "has enough funds")
#         r_ F..
#
#     ___ setCard card
#         ?  ?
#
#     ___ do_pay
#         __ __hF..
#             print("Bank:: Paying the merchant")
#             r_ T..
#         ____
#             print("Bank:: Sorry, not enough funds!")
#             r_ F...
#
# c_ DebitCard P..
#
#     ___ -
#         bank _ B..
#
#     ___ do_pay
#         card _ in.. ("Proxy:: Punch in Card Number: ")
#         b__.sC.. ?
#         r_ b__.d..
#
# c_ You
#
#     ___ -
#         print("You:: Lets buy the Denim shirt")
#         debitCard _ De..
#         isPurchased _ N..
#
#     ___ make_payment
#         isPurchased _ dC__.d..
#
#     ___ __del__
#         __ iP..
#             print("You:: Wow! Denim shirt is Mine :-)")
#         ____
#             print("You:: I should earn more :(")
#
# you _ Y..
# ?.m..