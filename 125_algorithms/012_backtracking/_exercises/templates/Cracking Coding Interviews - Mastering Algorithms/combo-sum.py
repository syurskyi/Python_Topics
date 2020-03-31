# ______ co..
#
# # Given a set of candidate numbers (candidates)
# # (without duplicates) and a target number (target),
# # find all unique combinations in candidates where the candidate numbers sums to target.
#
# # The same repeated number may be chosen from candidates unlimited number of times.
#
#
# # Example 1:
#
# # Input: candidates = [2,3,6,7], target = 7,
# # A solution set is:
# # [
# #   [7],
# #   [2,2,3]
# # ]
#
#
#
# # Example 2:
#
# # Input: candidates = [2,3,5], target = 8,
# # A solution set is:
# # [
# #   [2,2,2,2],
# #   [2,3,3],
# #   [3,5]
# # ]
#
# ___ combos candidates target path cur_sum candidate_index
# 	__ cur_sum __ t..
# 		r_ |p..
# 	____ ? t..
# 		r_   # list
#
# 	output _   ## list
#
# 	___ i __ ra.. c_i.. le. ca..
# 		cur _ ca..|?
# 		copy_path _ co__.d_c.. pa..
# 		?.ap.. cu.
#
# 		combinations _ c.. c.. t.. c_p.. c_s.. + cu. ?
#
# 		o.. +_ ?
#
# 	r_ ?
#
# ___ combo_sum c.. t..
# 	r_ c.. c.. t.. || 0, 0
#
# print(?([2,3,6,7], 7))
#
#
# print(?([2,3,5], 8))
#
#
#
#
#
