# # Pascal's Triangle II
# # Question: Given an index k, return the kth row of the Pascal's triangle.
# # For example, given k = 3, Return [1,3,3,1].
# # Note: Could you optimize your algorithm to use only O(k) extra space?
# # Solutions:
#
#
# c_ Solution
#     # @return a list of integers
#     ___ getRow  rowIndex
#         __ ? __ 0
#             r_  1
#         __ ? __ 1
#             r_ [1, 1]
#         result _ [1]
#         nextDivisor _ 1
#         nextMultiplier _ ?
#         ___ _ __ ra.. ? // 2
#             nextVal _ in. r.. -1 * n.. / n..
#             r__.ap.. ?
#             ? +_ 1
#             ? -_ 1
#         __ ? % 2 __ 1
#             r__.e.. r__ ||-1
#         ____
#             r__.e.. r__ -2||-1
#         r_ ?
#
#
# ? .? 3