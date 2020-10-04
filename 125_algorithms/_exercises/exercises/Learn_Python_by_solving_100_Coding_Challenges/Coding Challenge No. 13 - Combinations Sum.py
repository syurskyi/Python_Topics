# # Combinations Sum
# # Question: Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# # The same repeated number may be chosen from C unlimited number of times.
# # Note:
# # All numbers (including target) will be positive integers.
# # Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# # The solution set must not contain duplicate combinations.
# # For example, given candidate set 2,3,6,7 and target 7,
# # A solution set is:
# # [7] ; [2, 2, 3]
# # Solutions:
#
# c_ Solution
#     ___ combinationSum candidates target
#         ?.s..
#         res_  # list
#         ? ? ? 0 ?  # list)
#         r_ ?
#
#     ___ DFS candidates target start res intermedia
#         __ target__0
#             r__.ap.. i..
#             r_
#         ___ i __ ra.. s.. le. ?
#             __ ? < ? ?
#                 r_
#             ? ? ? - c..? i r.. i.. + ? ?
#         print ? .? [2,3,6,7],7