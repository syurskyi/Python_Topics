# # Combinations Sum II
# # Question: Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# # Each number in C may only be used once in the combination.
# # Note:
# # All numbers (including target) will be positive integers.
# # Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# # The solution set must not contain duplicate combinations.
# # For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# # A solution set is: [1, 7] ; [1, 2, 5] ; [2, 6] ; [1, 1, 6]
# # Solutions:
#
#
# c_ Solution
#     ___ combinationSum2  candidates target
#         __ no. ?
#             r_   # list
#         ?.s..
#         result _   # list
#         ? ? ?   # list, result)
#         r_ ?
#     ___ combination candidates target current result
#         s _ su. c.. __ c.. ____ 0
#         __ ? > t..
#             r_
#         ____ ? __ t..
#             r__.ap.. ?
#             r_
#         ____
#             i _ 0
#             w___ ? < le. ?
#                 ? ? ? + 1| ? ? + ? ? ?
#                 w___ ? + 1 < le. ? an. ? ? __ ? ? + 1
#                     ? +_ 1
#             ? +_ 1
#
#
# ? .? [10, 1, 2, 7, 6, 1, 5], 8