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
#         __ no. isi..? ?
#             k.. _ ? ?
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
#         p..
#
#     ___ _find_val curr key
#         p..
#
#     ___ delete_val key
#         p..
#
#     ___ _delete_val  curr prev is_left key
#         p..
#
# tree _ BSTDemo()
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
