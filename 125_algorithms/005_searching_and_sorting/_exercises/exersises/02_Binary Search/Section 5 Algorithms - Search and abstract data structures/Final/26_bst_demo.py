# # Final implementation
#
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
#                 _? ?.l..  ?
#
#     ___ in_order
#         _? r..
#         print("")
#
#     ___ _in_order curr
#         __ ?
#             _? ?.l..
#             print ?.d.. e.._" ")
#             _? ?.r..
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
#     ___ find_val ?
#         r_ _? r.. ?
#
#     ___ _find_val curr, key
#         __ ?
#             __ ? __ ?.d..
#                 r_ "Value found in tree"
#             ____ ? < ?.d..
#                 r_ _? ?.l.. ?
#             ____
#                 r_ _? ?.r.. ?
#         r_ "Value no. found in tree"
#
#     ___ min_right_subtree curr
#         __ ?.l.. __ N..
#             r_ ?
#         ____
#             r_ ? ?.l..
#
#     ___ delete_val key
#         _? r.. N.. N.. ?
#
#     ___ _delete_val curr prev is_left key
#         __ ?
#             __ ? __ ?.d..
#                 __ ?.l.. an. ?.r..
#                     min_child _ m.. ?.r..
#                     ?.d.. _ ?.d..
#                     _d.. ?.r.. ? F.. m__.d..
#                 ____ ?.l.. __ N.. an. ?.r.. __ N..
#                     __ p..
#                         __ i..
#                             p__.l.. _ N..
#                         ____
#                             p__.r.. _ N..
#                     ____
#                         r.. _ N..
#                 ____ ?.l.. __ N..
#                     __ p__:
#                         __ is_left
#                             p__.l.. _ ?.r..
#                         ____
#                             p__.r.. _ ?.r..
#                     ____
#                         r.. _ ?.r..
#                 ____
#                     __ p__
#                         __ i..
#                             p__.l.. _ ?.l..
#                         ____
#                             p__.r.. _ ?.l..
#                     ____
#                         r.. _ ?.l..
#             ____ ? < ?.d..
#                 _d.. ?.l.. ? T.. ?
#             ____ ? > ?.d..
#                 _d.. ?.r.. ? F.. ?
#         ____
#             print _*|? no. found in Tree")
#
# tree _ ?
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
