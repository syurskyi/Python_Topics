#
#
# c_ Node
#     ___  -  value
#         .left _ N..
#         .right _ N..
#         .data _ ?
#
#
# ___ insert root node
#     __ ? pa__ N..
#         ? _ ?
#         r_
#
#     __ ?.d.. < ?.d..
#         __ ?.r.. pa__ N..
#             ?.r.. _ ?
#         ____
#             i.. ?.r.. ?
#     ____
#         __ ?.l.. pa__ N..
#             ?.l.. _ ?
#         ____
#             i.. ?.l.. ?
#
#
# ___ preorder node
#     __ ? pa__ no. N..
#         print ?.d..
#         p.. ?.l..
#         p.. ?.r..
#
#
# ___ minValueNode node
#     w___?.l.. pa__ no. N..
#         node _ ?.l..
#     r_ ?
#
#
# ___ deleteNode node key
#     __ ? pa__ N..
#         r_ ?
#     # If the key to be deleted is smaller than the node's
#     # key then it lies in  left subtree
#     __ ? < ?.d..
#         ?.l.. _ d.. ?.l.. ?
#     # If the kye to be delete is greater than the node's key
#     # then it lies in right subtree
#     ____ ? > ?.d..
#         ?.r.. _ d.. ?.r.. ?
#     # If key is same as node's key, then this is the node
#     # to be deleted
#     ____
#         # Node with only one child or no child
#         __ ?.l.. pa__ N..
#             temp _ ?.r..
#             ? _ N..
#             r_ ?
#         ____ ?.r.. pa__ N..
#             temp _ ?.l..
#             ? _ N..
#             r_ ?
#
#         # Node with two children: Get the inorder successor
#         # (smallest in the right subtree)
#         temp _ m.. ?.r..
#         # Copy the inorder successor's content to this node
#         ?.d.. _ ?.d..
#         # Delete the inorder successor
#         ?.r.. _ d.. ?.r.. ?.d..
#
#     r_ ?
#
#
# #	           5
# #       /  	      \
# #     3	            7
# #   /   \        /     \
# #  2     4      6        8
# tree _ Node(5)
#
# insert(tree, Node(3))
#
#
# insert(tree, Node(2))
#
# insert(tree, Node(4))
#
# insert(tree, Node(7))
#
# insert(tree, Node(6))
#
# insert(tree, Node(8))
#
# deleteNode(tree, 7)
#
# #	           5
# #       /  	      \
# #     3	            8
# #   /   \        /     \
# #  2     4      6       None
#
#
# # 5 3 2 4 8 6
# preorder(tree)
