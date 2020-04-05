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
#     ___ min_right_subtree curr
#         __ ?.l.. __ N..
#             r_ ?
#         ____
#             r_ ? ?l..
#
#     ___ delete_val key
#         _? r.. N.. N.. k..
#
#     ___ _delete_val curr prev is_left key
#         __ ?
#             __ k.. __ ?.d..
#                 __ ?.l.. an. ?.r..
#                     min_child _ m_r_s.. ?.r..
#                     ?.d.. _ ?.d..
#                     _? ?.r.. ? F.. ?.d..
#                 ____ ?.l.. __ N.. an. ?.r.. __ N..
#                     __ p..
#                         __ i..
#                             p__.l.. _ N..
#                         ____
#                             p__.r.. _ N..
#                     ____
#                         root _ N..
#                 ____ ?.l.. __ N..
#                     __ p..
#                         __ i..
#                             p__.l.. _ ?.r..
#                         ____
#                             p__.r.. _ ?.r..
#                     ____
#                         root _ ?.r..
#                 ____
#                     __ p..
#                         __ i..
#                             p__.l.. _ ?.l..
#                         ____
#                             p__.r.. _ ?.l..
#                     ____
#                         root _ ?.l..
#             ____ k.. < ?.d..
#                 _? ?.l.. ? T.. k..
#             ____ k.. > ?.d..
#                 _? ?.r.. ? F.. k..
#         ____
#             print _*|k.. not found in Tree")
#
# tree _ BSTDemo()
# tree.insert("F")
# tree.insert("C")
# print("Test deleting leaf node which is left child of parent")
# tree.in_order()
# tree.delete_val("C")
# tree.in_order()
# tree.insert("G")
# print("Test deleting leaf node which is right child of parent")
# tree.in_order()
# tree.delete_val("G")
# tree.in_order()
# tree.insert("A")
# print("Test deleting parent/root node which has one child")
# tree.in_order()
# tree.delete_val("F")
# tree.in_order()
# print("Test deleting root node which has no children")
# tree.in_order()
# tree.delete_val("A")
# tree.in_order()
# tree.insert("F")
# tree.insert("C")
# tree.insert("G")
# tree.insert("A")
# tree.insert("B")
# tree.insert("K")
# tree.insert("E")
# tree.insert("H")
# tree.insert("D")
# tree.insert("I")
# tree.insert("M")
# tree.insert("J")
# tree.insert("L")
# tree.in_order()
# tree.delete_val("F")
# tree.in_order()
# tree.in_order()
# tree.delete_val("K")
# tree.in_order()
# tree.in_order()
# tree.delete_val("C")
# tree.in_order()
# tree.delete_val("Z")
