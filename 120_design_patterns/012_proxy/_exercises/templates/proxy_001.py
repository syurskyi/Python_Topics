# #!/usr/bin/env python
#
# """
# *TL;DR80
# Provides an interface to resource that is expensive to duplicate.
# """
#
# ____ -f ______ p...
# ______ ti__
#
#
# c_ SalesManager
#     ___ talk
#         print("Sales Manager ready to talk")
#
#
# c_ Proxy
#     ___ -_
#         busy _ 'No'
#         sales _ N..
#
#     ___ talk
#         print("Proxy checking for Sales Manager availability")
#         __ busy __ 'No':
#             sales _ S..
#             ti__.sl.. (0.1)
#             ?.t..
#         ____
#             ti__.sl.. 0.1
#             print("Sales Manager is busy")
#
#
# c_ NoTalkProxy P..
#     ___ talk
#         print("Proxy checking for Sales Manager availability")
#         ti__.sl.. 0.1
#         print("This Sales Manager will not talk to you",
#               "whether he/she is busy or not")
#
#
# __ _______ __ ______
#     p _ P..
#     ?.t..
#     ?.b.. _ 'Yes'
#     ?.t..
#     ? _ N..
#     ?.t..
#     ?.b.. _ 'Yes'
#     ?.t..
#
# ### OUTPUT ###
# # Proxy checking for Sales Manager availability
# # Sales Manager ready to talk
# # Proxy checking for Sales Manager availability
# # Sales Manager is busy
# # Proxy checking for Sales Manager availability
# # This Sales Manager will not talk to you whether he/she is busy or not
# # Proxy checking for Sales Manager availability
# # This Sales Manager will not talk to you whether he/she is busy or not
