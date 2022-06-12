# _______ p__
# ____ ? _______ ?
#
#
# # write your pytest functions below, they need to start with test_
# ?p__.f..
# ___ einstein
#     r.. ? 'Einstein', 100
#
#
# ?p__.f..
# ___ socrates
#     r.. ? 'Socrates', 0
#
#
# ___ add_transactions acct, values
#     ___ v __ ?
#         ?.a.. ?
#
#
# ___ test_account_create einstein
#     ... isi.. ? A..
#     ... ?.b.. __ 100
#     ... s.. ? __ 'Account of Einstein with starting amount: 100'
#     ... r..  ? __ "Account('Einstein', 100)"
#     hector ? 'Hector')
#     ... r.. ? __ "Account('Hector', 0)"
#
#
# ___ test_account_transaction einstein
#     ... ? .b.. __ 100
#     ? .a.. 50
#     ... ? .b.. __ 150
#     ? .a.. -75
#     ... ? .b.. __ 75
#     ... l..(? ) __ 2
#
#
# ___ test_account_bad_transaction socrates
#     ... ?.b.. __ 0
#     w__ p__.r.. V... __ exp
#         ?.a.. 3.14
#     ... 'please use int for amount' __ s.. ?.v..
#     ... ?.b.. __ 0
#
#
# ___ test_account_comparisons(einstein, socrates
#     ... ?  > ?
#     ? ?, [10, 20, 30
#     ... ?.b.. __ 60
#     ... ? 1 __ 20
#     ?.a.. 40
#     ... ?  __ ?
#     ... n.. ?  < ?
#
#
# ___ test_account_merge_accounts einstein socrates
#     ... ? .b.. __ 100 a.. ?.b.. __ 0
#     ? ? , [50, -75
#     ? ?, [10, 20, 30
#     ... ? .b.. __ 75 a.. ?.b.. __ 60
#     pythagoras ?  + ?
#     ... ?.b.. __ 135
#     ... s.. ? __ 'Account of Einstein&Socrates with starting amount: 100'
#     ... l.. ? __ 5
#     ... ? 1 __ -75
#
#
# ___ test_account_bad_merge_accounts einstein, socrates
#     ?(? , [50, -75
#     ?(?, [10, 20, 30
#     kelvin ? 'Kelvin', 20
#     ... ?.b.. __ 20
#     armstrong ? + ?  + ?
#     ... ?.b.. __ 155
#     ... s.. ? __ 'Account of Kelvin&Einstein&Socrates with starting amount: 120'
