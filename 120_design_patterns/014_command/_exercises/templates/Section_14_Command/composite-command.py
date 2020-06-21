# # Composite Command a.k.a. Macro
# # also: Composite design pattern ;)
#
# ______ u..
# ___ a.. ______ A.. a..
# ___ e.. ______ E..
#
#
# c_ BankAccount:
#     OVERDRAFT_LIMIT _ -500
#
#     ___ - balance_0
#         ?  ?
#
#     ___ deposit amount
#         b... +_ ?
#         print _*Deposited |?, balance _ |b..
#
#     ___ withdraw amount
#         __ b... - a.. >_ BA___.O...
#             b.. -_ a..
#             print _*Withdrew |?, balance _ |b..
#             r_ T...
#         r_ F..
#
#     ___ -s
#         r_ _*Balance _ |b..
#
#
# c_ Command A..
#     ___ -
#         success _ F..
#
#     ___ invoke
#         p..
#
#     ___ undo
#         p..
#
#
# c_ BankAccountCommand C..
#     ___ -  account action amount
#         s__. -
#         am.. _ am..
#         ac.. _ ac..
#         acc.. _ acc..
#
#     c_ Action E..
#         DEPOSIT _ 0
#         WITHDRAW _ 1
#
#     ___ invoke
#         __ action __ A___.D..
#             acc__.d.. am..
#             success _ T...
#         ____ action __ A__.W..
#             success _ acc__.wi.. am..
#
#     ___ undo
#         __ no. success
#             r_
#         # strictly speaking this is not correct
#         # (you don't undo a deposit by withdrawing)
#         # but it works ___ this demo, so...
#         __ action __ A_.D...
#             acc__.wi.. am..
#         ____ action __ A___.W..
#             acc__.d.. am..
#
#
# # try using this before using MoneyTransferCommand!
# c_ CompositeBankAccountCommand C.. li..
#     ___ - items_||
#         s___ . -
#         ___ i in ?
#             ap.. ?
#
#     ___ invoke
#         ___ x __ ?
#             ?.in..
#
#     ___ undo
#         ___ x __ rev.. ?
#             ?.u..
#
#
# c_ MoneyTransferCommand CBAC..
#     ___ -  from_acct, to_acct, amount
#         s___ . - ||
#             BAC.. f_a..
#                                BAC__.A___.W..
#                                am.
#             BAC__(t_a..
#                                BAC__.A___.D..,
#                                am..
#
#     ___ invoke
#         ok _ T...
#         ___ cmd __ ?
#             __ ?
#                 ?.in..
#                 ok _ ?.s..
#             ____
#                 ?.s... _ F..
#         success _ ?
#
#
# c_ TestSuite(unittest.TestCase):
#     ___ test_composite_deposit(self):
#         ba _ BankAccount()
#         deposit1 _ BAC__(ba, BAC__.A___.D.., 1000)
#         deposit2 _ BAC__(ba, BAC__.A___.D.., 1000)
#         composite _ CompositeBankAccountCommand([deposit1, deposit2])
#         composite.invoke()
#         print(ba)
#         composite.undo()
#         print(ba)
#
#     ___ test_transfer_fail(self):
#         ba1 _ BankAccount(100)
#         ba2 _ BankAccount()
#
#         # composite isn't so good because of failure
#         amount _ 1000  # try 1000: no transactions should happen
#         wc _ BAC__(ba1, BAC__.A___.WITHDRAW, amount)
#         dc _ BAC__(ba2, BAC__.A___.D.., amount)
#
#         transfer _ CompositeBankAccountCommand([wc, dc])
#
#         transfer.invoke()
#         print('ba1:', ba1, 'ba2:', ba2)  # end up in incorrect state
#         transfer.undo()
#         print('ba1:', ba1, 'ba2:', ba2)
#
#     ___ test_better_tranfer(self):
#         ba1 _ BankAccount(100)
#         ba2 _ BankAccount()
#
#         amount _ 1000
#
#         transfer _ MoneyTransferCommand(ba1, ba2, amount)
#         transfer.invoke()
#         print('ba1:', ba1, 'ba2:', ba2)
#         transfer.undo()
#         print('ba1:', ba1, 'ba2:', ba2)
#         print(transfer.success)
