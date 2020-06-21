# c_ Node o..
#
#     ___ - character
#         ? ?
#         leftNode _ N..
#         middleNode _ N..
#         rightNode _ N..
#         value _ 0
#
#
# c_ TST object
#
#     ___ -
#         rootNode _ N..
#
#     ___ put key value
#         rootNode _ pI.. r.. key value 0
#
#     ___ putItem node key value index
#
#         c _ k..|i..
#
#         __ ? __ N..
#             ? _ N.. ?
#
#         __ c < ?.c..
#             ?.l.. _ p..  ?.l.. k.. v.. i..
#         ____ c > ?.ch..
#             ?.r.. _ p.. ?.r.. k.. v.. i..
#         ____ i.. < le. k.. - 1
#             ?.m.. _ p.. ?.m.. k.. v.. i.. + 1
#         ____
#             ?.v.. _ v..
#
#         r_ ?
#
#     ___ get key
#
#         ? _ g.. r.. k.. 0
#
#         __ ? __ N..
#             r_ -1
#
#         r_ ?.v..
#
#     ___ getItem ? k.. i..
#
#         __ ? __ N..
#             r_ N..
#
#         c _ key|i..
#
#         __ ? < ?.c..
#             r_ g.. ?.l.. k.. i..
#         ____ ? > ?.c..
#             r_ g.. ?.r.. k.. i..
#         ____ i.. < le. k.. - 1
#             r_ getItem(?.m.. k.. i.. + 1
#         ____
#             r_ ?
#
#
# __ _______ __ ________
#     tst _ ?
#
#     ?.p..("apple", 100)
#     ?.p..("orange", 200)
#
#     print(?.g..("orange"))
