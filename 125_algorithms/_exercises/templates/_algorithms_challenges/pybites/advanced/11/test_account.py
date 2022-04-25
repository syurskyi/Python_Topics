# _______ p__
#
# ____ ? _______ ?
#
# checking ? 'Checking'
# saving ? 'Saving', 10
#
#
# ___ test_account_balance
#     ... ?.s.. __ 0
#     ? + 10
#     ... ?.b.. __ 10
#
#     ... ?.s..__ 10
#     w__ p__.r.. T..
#         ? - 'a'
#     ? - 5
#     ... ?.b.. __ 5
#
#
# ___ test_account_comparison
#     ... ? > ?
#     ... ? >_ ?
#     ... ? < ?
#     ... ? <_ ?
#     ? + 5
#     ... ? __ ?
#
#
# ___ test_account_len
#     ? + 10
#     ? + 3
#     ? - 8
#     ... l.. ? __ 4
#
#
# ___ test_account_indexing_iter
#     ... ? 0 __ 10
#     ... ? -1 __ -8
#     ... l.. ? __ [10, 10, 3, -8]
#
#
# ___ test_account_str
#     ... s.. ? __ 'Checking account - balance: 15'
#     ... s.. ? __ 'Saving account - balance: 10'
#     ? + 5
#     ... s.. ? __ 'Saving account - balance: 15'