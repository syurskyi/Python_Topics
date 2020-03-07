# #=======================================================================================================================
# ____ a.. ______ A.. a..
# #  Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ Chef
#     """chef"""
#
#     ___ steamFood originalMaterial
#         print("@ steaming .."  ?
#         r_ "Steamed" + ?
#
#     ___ stirFriedFood originalMaterial
#         print("@ s being fried ..."  ?
#         r_ "Spicy Fried" + ?
#
# c_ Order m..
#     """Order"""
#
#     ___ - name originalMaterial
#         _chef _ C..
#         _name _ ?
#         _originalMaterial _ ?
#
#     ___ getDisplayName
#         r_ _n.. + _o...
#
#     ??
#     ___ processingOrder
#         p..
#
# c_ SteamedOrder O..
#     """Steamed"""
#
#     ___ - originalMaterial
#         s___ . - "Steamed" o..
#
#     ___ processingOrder
#         __(_chef __ no. N..
#             r_ _c__.sF.. _o...
#         r_ ""
#
#
# c_ SpicyOrder O
#     """Spicy Fried"""
#
#     ___ - oM..
#         s___ . - "Spicy Fried", o..
#
#     ___ processingOrder
#         __ _c.. __ no. N..
#             r_ _c__.sFF.. _o..
#         r_ ""
#
#
# c_ Waiter
#     """Waiter"""
#
#     ___ - name
#         __?  ?
#         __order _ N..
#
#     ___ receiveOrder order
#         __order _ order
#         print("Waiter @: Your order for @  has been received, please be patient"  __n.. o___.gDN..
#
#     ___ placeOrder
#         food _ __o__.pO..
#         print("Waite @  Your meal @ is ready, please use it slowly!"  __n.. f..
#
#
#
# # c_ Customer:
# #     "Customer"
# #
# #     ___ __init__(self, name):
# #         __name _ name
# #
# #     ___ order
#
# # Version 2.0
# #=======================================================================================================================
# # Code framework
# #==============================
# ____ a.. ______ A... a..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ Command m..
#     """Command's Abstract Class"""
#
#     ??
#     ___ execute
#         p..
#
# c_ CommandImpl C..
#     """The concrete implementation c_ of the command"""
#
#     ___ - receiver
#         __?  ?
#
#     ___ execute
#         __r__.dS..
#
# c_ Receiver
#     """Recipient of the command"""
#
#     ___ doSomething
#         print("do something...")
#
# c_ Invoker
#     """Scheduler"""
#
#     ___ -
#         __command _ N..
#
#     ___ setCommand command
#         __?  ?
#
#     ___ action
#         __ __c.. __ no. N..
#             __c___.ex..
#
#
# # Framework-based implementation
# #==============================
#
# # Test
# #=======================================================================================================================
#
# ___ Order
#     waiter _ ?("Anna")
#     steamedOrder _ ?("Hairy crab")
#     print(" Customer David I want a copy @"  ?.gDN..
#     w__.rO.. sO..
#     w__.pO..
#     print()
#
#     spicyOrder _ ?("Hair crab")
#     print("Customer Tony I want a copy @"  ?.gDN..
#     w__.rO.. ?
#     w__.pO..
#
#
# ___ client
#     invoker _ I...
#     command _ CI.. R..
#     ?.sC.. ?
#     ?.a..
#
#
# # Order()
# client()
#
