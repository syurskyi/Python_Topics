#
#
# c_ Node
#     ___  -  value
#         .left _ N..
#         .right _ N..
#         .data _ ?
#
#
# ___ postorder node
#     __ ? pa__ no. N..
#         ? ?.l..
#         ? ?.r..
#         print(?.d..
#
#
# # create root
# root _ N.. 4
# ''' following is the tree after above statement
# 	    4
# 	  /   \
# 	None  None
# '''
#
# ?.left _ ? 5
# ?.right _ ? 6
#
# ''' 5 and 6 become left and right children of 1
# 		           4
# 		       /       \
# 		      5	        6
# 	      /  \      /   \
#       None None  None  None
# '''
#
#
# ?.l__.l.. _ ? 7
# '''
# 7 becomes left child of 5
# 		           4
# 		       /       \
# 		      5	        6
# 	      /  \      /   \
#        7   None  None  None
#       / \
#   None   None
#
# '''
# postorder ?
#
# #              4
# #          /       \
# #         5         6
# #       /  \      /   \
# #      7   None  None  None
# #     / \
# # None   None
