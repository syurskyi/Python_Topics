# # -*- coding: utf-8 -*-
# ____ a.. _______ A... a..
#
# # Base Interface's
# c_ SavinAccount o..
#     """Abstract class
#     """
#     m...
#
# c_ SavinAccountWithWithdrawal S...
#     """Abstract class
#     """
#     m...
#
#     ??
#     ___ withdrawal ammount
#         r_ N..
#
# c_ SavinAccountWithoutWithdrawal S..
#     """Abstract class
#     """
#     m..
#
#
# # Child Class
#
# c_ RegularSavingAccount S..
#
#     ___ withdrawal  ammount
#         r_ ?
#
# c_ SalarySavingAccount S..
#
#     ___ withdrawal  ammount
#         r_ ?
#
# c_ FixDepositeSavingAccount S..
#     ___ -
#         p..
#
#
# # Decorator
#
# ___ verifiy_withdrawal func
#     ___ inner $
#         __ no. iss.. ty.. ar.. 1 , S.. : print("@ is a type @, the function need a SavinAccountWithWithdrawal type"  ar.. 1 ty.. ar.. 1||||; exit(0)
#         r_ f.. $
#     r_ i..
#
#
# # Context Manager
#
# c_ AccountManager o..
#
#     ?v..
#     ___ withdrawFromAccount account ammount
#         print a__.w.. am..
#
#
# __ ______ __ ______
#     regular_saving_account _ R...
#     salary_saving_account _ S...
#     fix_deposite_saving_account _ F..
#     ammount _ 100
#
#     account_manager _ A..
#     ?.w____ r___ a...
#     ?.w____ s____ a...
#     ?.w____ f____ a...
#
#
