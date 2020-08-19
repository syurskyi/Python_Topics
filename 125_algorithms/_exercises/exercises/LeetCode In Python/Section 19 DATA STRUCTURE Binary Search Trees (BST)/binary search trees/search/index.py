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
#         root _ ?
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
# ___ search node key
#     print("Current Node is: " ?.d..
#     __ ? pa__ N..
#         print("No node found")
#         r_ N..
#     __ ?.d.. __ ?
#         print("Node found !")
#         r_ ?
#
#     __ ?.d.. < ?
#         r_ ? ?.r.. ?
#
#     r_ ? ?.l.. ?
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
# search(tree, 8)
