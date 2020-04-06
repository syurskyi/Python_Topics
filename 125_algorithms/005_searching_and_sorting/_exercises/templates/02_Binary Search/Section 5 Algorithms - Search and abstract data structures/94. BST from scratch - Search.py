# c_ Node
#     ___ - key
#         data _ ?
#         left_child _ N..
#         right_child _ N..
#
# c_ BSTDemo
#     ___ -
#         root _ N..
#
#     ___ insert key
#         __ no. isi.. ? ?
#             ? _ ? ?
#         __ r.. __ N..
#             r.. _ ?
#         ____
#             _? r.. ?
#
#     ___ _insert curr key
#         __ ?.d.. > ?.d..
#             __ ?.r.. __ N..
#                 ?.r.. _ ?
#             ____
#                 _? ?.r.. ?
#         ____ ?.d.. < ?.d..
#             __ ?.l.. __ N..
#                 ?.l.. _ ?
#             ____
#                 _? ?.l.. ?
#
#     ___ in_order
#         _? r..
#         print("")
#
#     ___ _in_order curr
#         __ ?
#             _? ?.l..
#             print ?.d.. e.._" "
#             _? ?.r..
#
#     ___ pre_order
#         p..
#
#     ___ _pre_order curr
#         p..
#
#     ___ post_order
#         p..
#
#     ___ _post_order curr
#         p..
#
#     ___ find_val key
#         r_ _? r.. ?
#
#     ___ _find_val curr ?
#         __ ?
#             __ ? __ ?.d..
#                 r_ "Value found in tree"
#             ____ ? < ?.d..
#                 r_ _? ?.l.. ?
#             ____
#                 r_ _? ?.r.. ?
#         r_ "Value no. found in tree"
#
#     ___ delete_val ?
#         p..
#
#     ___ _delete_val curr prev is_left ?
#         p..
#
# tree _ BSTDemo()
# tree.insert("H")
# tree.insert("D")
# tree.insert("I")
# tree.insert("M")
# tree.insert("J")
# tree.insert("L")
# tree.insert("F")
# tree.insert("C")
# tree.insert("G")
# tree.insert("A")
# tree.insert("B")
# tree.insert("K")
# tree.insert("E")
# tree.in_order()
# print(tree.find_val("E"))
# print(tree.find_val("J"))
# print(tree.find_val("Z"))
