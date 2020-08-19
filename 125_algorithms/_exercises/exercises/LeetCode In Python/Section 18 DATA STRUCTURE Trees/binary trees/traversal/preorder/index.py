#
#
# c_ Node
#     ___  -  value
#         .left _ N..
#         .right _ N..
#         .data _ ?
#
#
# ___ preorder node
#     __ ? pa__ no. N..
#         print ?.d..
#         ? ?.l..
#         ? ?.r..
#
#
# # create root
# root _ ? 4
# ''' following is the tree after above statement
# 	    4
# 	  /   \
# 	None  None
# '''
#
# ?.l.. _ ? 5
# ?.r.. _ ? 6
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
# ?.l__.l.. _ ?(7)
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
# ? ?
#
# #              4
# #          /       \
# #         5         6
# #       /  \      /   \
# #      7   None  None  None
# #     / \
# # None   None
