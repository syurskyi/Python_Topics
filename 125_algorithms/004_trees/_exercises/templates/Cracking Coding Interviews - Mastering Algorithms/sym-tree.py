# c_ Node
# 	___ -  val left_N.. right_N..
# 		? ?
# 		? ?
# 		? ?
#
# # Given a binary tree, check whether it is a mirror of itself
# # (ie, symmetric around its center).
#
# # Example 1
#
# #     1
# #    / \
# #   2   2
# #  / \ / \
# # 3  4 4  3
#
# # => True
#
# # Example 2
#
# #   1
# #  / \
# # 2   2
# #  \   \
# #  3    3
#
# # => False
#
# ___ sym_tree_helper root1 root2
# 	__ _1 __ N.. an. _2 __ N..
# 		r_ T..
# 	____ _1 __ N.. o. _2 __ N..
# 		r_ F..
# 	____ _1.v.. !_ _2.v..
# 		r_ F..
#
# 	r_ ? _1.r.. _2.l..| an. ? _1.l.. _2.r..
#
# ___ sym_tree root
# 	__ ? __ N..
# 		r_ T..
#
# 	r_ ? ?.l.. ?.r..
#
# root1 = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))
#
# print(sym_tree(root1))
#
# root2 = Node(1, Node(2, N.., Node(3)), Node(2, N.., Node(3)))
# print(sym_tree(root2))