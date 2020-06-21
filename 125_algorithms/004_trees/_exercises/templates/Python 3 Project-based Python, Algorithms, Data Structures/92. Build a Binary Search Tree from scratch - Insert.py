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
#         p..
#
#     ___ _in_order curr
#         p..
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
#     ___ _delete_val curr prev is_left key
#         p..
#
# tree _ BSTDemo()
# tree.insert("F")
# print(tree.root.data)
# tree.insert("C")
# print(tree.root.left_child.data)
# tree.insert("G")
# print(tree.root.right_child.data)
# tree.insert("A")
# print(tree.root.left_child.left_child.data)
# tree.insert("B")
# print(tree.root.left_child.left_child.right_child.data)
# tree.insert("K")
# print(tree.root.right_child.right_child.data)
# tree.insert("H")
# print(tree.root.right_child.right_child.left_child.data)
