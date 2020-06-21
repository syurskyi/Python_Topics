# ___ a.. ______ A..
# ___ e..  ______ E..
#
#
# c_ BankAccount
#     OVERDRAFT_LIMIT _ -500
#
#     ___ - balance_0
#         ?  ?
#
#     ___ deposit  amount
#         b___ +_ ?
#         print _*Deposited |?, balance _ |b..
#
#     ___ withdraw amount
#         __ b... - ? >_ BA___.O...
#             b... -_ a..
#             print _*Withdrew |a..., balance _ |b...
#             r_ T..
#         r_ F..
#
#     ___ -s
#         r_ _*Balance _ |b..
#
#
# # optional
# c_ Command A..
#     ___ invoke
#         p..
#
#     ___ undo(
#         p..
#
#
# c_ BankAccountCommand C..
#     ___ -  account, action, amount
#         am.. _ am..
#         ac.. _ ac..
#         acc.. _ acc..
#         success _ N..
#
#     c_ Action E..
#         DEPOSIT _ 0
#         WITHDRAW _ 1
#
#     ___ invoke
#         __ action __ A__.D..
#             acc___.de.. am..
#             success _ T..
#         ____ action __ A__.W..
#             success _ acc___.wi.. am..
#
#     ___ undo
#         __ no. success
#             r_
#         # strictly speaking this is not correct
#         # (you don't undo a deposit by withdrawing)
#         # but it works for this demo, so...
#         __ action __ A__.D..
#             acc__.wi.. am..
#         ____ action __ A___.W..
#             acc__.de.. am..
#
#
# __ _______ __ ______
#     ba _ BA..
#     cmd _ BAC.. ? BAC___.A__.DE.. 100
#     ?.in..
#     print('After $100 deposit:' b.
#
#     c__.un..
#     print('$100 deposit undone:' b.
#
#     illegal_cmd _ BAC.. b. BAC__.A__.W.. 1000
#     ?.in..
#     print('After impossible withdrawal:', b.
#     i_c_.un..
#     print('After undo:', b.
#
#
