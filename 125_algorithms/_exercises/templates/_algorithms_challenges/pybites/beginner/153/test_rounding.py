# _______ p__
#
# ____ ? _______ ?
#
# transactions1  [2.05, 3.55, 4.50, 10.76, 100.25]
# transactions2  [1.55, 9.17, 5.67, 6.77, 2.33]
# transactions_including_negatives  transactions2 + [-2.05]
#
#
# ?p__.m__.p. "transactions, up_arg, expected"
#     _1 T.. 3, 4, 5, 11, 101
#     _1 F.. 2, 3, 4, 10, 100
#     _2 T.. 2, 10, 6, 7, 3
#     _2 F.. 1, 9, 5, 6, 2
#     ? F.. 1, 9, 5, 6, 2, -3
#
# ___ test_round_up_or_down transactions, up_arg, expected
#     ... ? ? __ ?