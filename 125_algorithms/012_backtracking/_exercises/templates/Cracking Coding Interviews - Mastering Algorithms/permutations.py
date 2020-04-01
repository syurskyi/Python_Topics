# ______ co..
# # Given a collection of distinct integers, return all possible permutations.
#
# # Example:
#
# # Input: [1,2,3]
# # Output:
# # [
# #   [1,2,3],
# #   [1,3,2],
# #   [2,1,3],
# #   [2,3,1],
# #   [3,1,2],
# #   [3,2,1]
# # ]
#
# ___ permutation_recursive nums path
# 	__ le. ? __ 0
# 		r_ |?
#
# 	output _    # list
#
# 	___ i __ ra.. le. ?
# 		copy_path _ co__.d_c.. ?
# 		?.ap.. n..|?
# 		permutations _ ? n..|:? + n..|? + 1: ?
#
# 		o.. +_ ?
#
# 	r_ ?
#
# ___ permute nums
# 	r_ ? ? ||
#
# print(?([1, 2, 3, 4, 5, 6]))
