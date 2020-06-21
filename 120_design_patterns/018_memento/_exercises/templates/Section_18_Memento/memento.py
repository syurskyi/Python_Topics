# c_ Memento
#     ___ - balance
#         ?  ?
#
#
# c_ BankAccount
#     ___ - balance_0
#         ?  ?
#
#
#     ___ deposit amount
#         balance +_ ?
#         r_ M.. b..
#
#     ___ restore memento
#         balance _ ?.b...
#
#     ___ -s
#         r_ _*Balance _ |b..'
#
#
# __ _______ __ ______
#     ba _ B.. 100
#     m1 _ ?.de.. 50
#     m2 _ ?.de.. 25
#     print ?
#
#     # restore to m1
#     ?.re.. m1
#     print ?
#
#     # restore to m2
#     ?.re.. m2
#     print ?