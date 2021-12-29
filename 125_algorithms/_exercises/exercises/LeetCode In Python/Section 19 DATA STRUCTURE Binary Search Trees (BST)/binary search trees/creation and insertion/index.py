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
#             ? ?.r.. ?
#     ____
#         __ ?.l.. pa__ N..
#             ?.l.. _ ?
#         ____
#             ? ?.l.. ?
#
#
# ___ preorder node
#     __ ? pa__ no. N..
#         print ?.d..
#         ? ?.l..
#         ? ?.r..
#
#
# #	         5
# #       /  	      \
# #     3	            7
# #   /   \        /     \
# #  2     4      6        8
# tree _ Node(5)
#
# #	         5
# #       /  	      \
# #     None	       None
#
# insert(tree, Node(3))
#
# #	         5
# #       /  	      \
# #     3	            None
#
# insert(tree, Node(2))
#
# #	         5
# #       /  	      \
# #     3	            None
# #   /
# #  2
# insert(tree, Node(4))
#
# #	         5
# #       /  	      \
# #     3	            None
# #   /   \
# #  2     4
# insert(tree, Node(7))
#
# #	         5
# #       /  	      \
# #     3	            7
# #   /   \
# #  2     4
# insert(tree, Node(6))
#
# #	         5
# #       /  	      \
# #     3	            7
# #   /   \        /
# #  2     4      6
# insert(tree, Node(8))
#
# #	         5
# #       /  	      \
# #     3	            7
# #   /   \        /     \
# #  2     4      6        8
#
#
# # 5 3 2 4 7 6 8
# preorder(tree)
