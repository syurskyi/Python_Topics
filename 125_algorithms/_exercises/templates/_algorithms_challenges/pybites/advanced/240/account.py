# # source: https://dbader.org/blog/python-dunder-methods
# ____ f.. _______ total_ordering
#
#
# ??
# c_ Account
#     'A simple account class'
#
#     ___ -  owner amount=0
#         'This is the constructor that lets us create objects from this class'
#         ? ?
#         ? ?
#         _transactions    # list
#
#     ___  -r
#         r.. Account @@@, @@@ .f.. ? ?
#
#     ___ -s
#         r.. Account of @ with starting amount: @.f.. ? ?
#
#
#     ___ add_transaction  amount
#         __ n.. isi.. ? i..
#             r.. V... 'please use int for amount')
#         _?.a.. ?
#
#     $
#     ___ balance
#         r.. ? + s.. _?
#
#     ___ -l
#         r.. l.. _?
#
#     ___ -g  position
#         r.. _transactions ?
#
#     ___ -e  other
#         r.. b.. __ ?.b..
#
#     ___ -l  other
#         r.. b.. < ?.b..
#
#     ___ -a  other
#         owner @&@.f.. ? ?.o..
#         start_amount a.. + ?.a..
#         acc A.. ? ?
#         ___ t __ l.. ____ + l.. ?
#             ?.a.. ?
#         r.. ?