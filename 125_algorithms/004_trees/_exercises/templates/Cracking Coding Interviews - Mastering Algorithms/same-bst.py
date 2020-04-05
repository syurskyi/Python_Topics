# c_ Node
# 	___ - val left_N.. right_N..
# 		? ?
# 		? ?
# 		? ?
#
# # Given two binary trees, write a function to check
# # if they are the same or not.
#
# # Two binary trees are considered the same if they are
# # structurally identical and the nodes have the same value.
#
#
# # Example 1:
#
# # Input:     1         1
# #           / \       / \
# #          2   3     2   3
#
# # Output: true
#
# root1 = Node(1, Node(2), Node(3))
# root2 = Node(1, Node(2), Node(3))
#
#
# # Example 2:
#
# # Input:     1         1
# #           /           \
# #          2             2
#
# # Output: false
#
# root3 = Node(1, Node(2), None)
# root4 = Node(1, None, Node(2))
#
# # Example 3:
#
# # Input:     1         1
# #           / \       / \
# #          2   1     1   2
#
# # Output: false
#
# root5 = Node(1, Node(2), Node(1))
# root6 = Node(1, Node(1), Node(2))
#
# ___ same_tree root1 root2
# 	__ _1 __ N.. an. _2 __ N..
# 		r_ T..
# 	____ _1 __ N.. o. _2 __ N..
# 		r_ F..
# 	____ _1.v.. !_ _2.v..
# 		r_ F..
#
# 	r_ ? _1.l.. _2.l..| an. ? _1.r.. _2.r..
#
#
# print(?(root1, root2))
# print(?(root3, root4))
# print(?(root5, root6))
#
#
#
#
#
#
#
#
#
