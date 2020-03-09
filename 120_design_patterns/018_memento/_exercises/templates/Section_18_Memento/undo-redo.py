# c_ Memento
#     ___ - balance
#         ?  ?
#
#
# c_ BankAccount
#     ___ - balance_0
#         ?  ?
#         changes _ |M.. ?
#         current _ 0
#
#
#     ___ deposit amount
#         b.. +_ ?
#         m _ M.. b..
#         ch__.ap.. ?
#         cu__ +_ 1
#         r_ m
#
#     ___ restore memento
#         __ ?
#             balance _ ?.b..
#             ch__.ap.. ?
#             current _ le. ch.. -1
#
#     ___ undo
#         __ current > 0
#             ? -_ 1
#             m _ ch__|?
#             balance _ m.b..
#             r_ m
#         r_ N..
#
#     ___ redo
#         __ current + 1 < le. ch..
#             ? +_ 1
#             m _ ch__|?
#             balance _ m.b..
#             r_ m
#         r_ N..
#
#     ___ -s
#         r_ f'Balance _ |b..
#
#
# __ _______ __ ______
#     ba _ BA.. 100
#     ?.d.. 50
#     ?.d.. 25
#     print(?)
#
#     ?.u..
#     print _*Undo 1: |?
#     ?.u..
#     print _*Undo 2: |?
#     ?.r..
#     print _*Redo 1: |?
