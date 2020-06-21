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
#         __ no. isi.. ? N..
#             k.. _ N.. ?
#         __ r.. __ N..
#             ? _ key
#         ____
#             _? r.. k..
#
#     ___ _insert curr key
#         __ k__.d.. > ?.d..
#             __ ?.right_child __ N..
#                 ?.right_child _ k..
#             ____
#                 _? ?.r.. k..
#         ____ k__.d.. < ?.d..
#             __ ?.l.. __ N..
#                 ?.l.. _ k..
#             ____
#                 _? ?.l.. k..
#
#     ___ in_order
#         _i.. r..
#         print("")
#
#     ___ _in_order curr
#         __ ?
#             _i.. ?.l..
#             print ?.d.. e.._" "
#             _i.. ?.r..
#
#     ___ pre_order
#         '''root, left, right'''
#         p..
#
#     ___ _pre_order curr
#         p..
#
#     ___ post_order
#         '''left, right, root'''
#         p..
#
#     ___ _post_order curr
#         p..
#
#     ___ find_val key
#         r_ _? ? ?
#
#     ___ _find_val curr key
#         __ ?
#             __ k.. __ ?.d..
#                 r_ "Value found in tree"
#             ____ k.. < ?.d..
#                 r_ _? ?.l.. k..
#             ____
#                 r_ _? ?.r.. k..
#         r_ "Value not found in tree"
#
#     ___ delete_val key
#         p..
#
#     ___ _delete_val curr prev is_left key
#         p..
#
# tree = BSTDemo()
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
