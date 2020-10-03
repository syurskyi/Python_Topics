# # Palindrome Partitioning
# # Question: Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# # For example: given s = "aab"
# # Return [ ["aa","b"], ["a","a","b"] ].
# # Solutions:
#
#
# c_ Solution
#     # @param s, a string
#     # @return a boolean
#     ___ _isPalindrome  s
#         begin end _ 0, le. ? - 1
#         w___ ? < ?
#             __ ? ? !_ ? ?
#                 r_ F..
#             ____
#                 ? +_ 1
#                 ? -_ 1
#         r_ T..
#
#     # @param s, a string
#     # @return a list of lists of string
#
#     ___ partition  s
#         __ le. ? __ 0
#             r_   # list
#         __ le. ? __ 1
#             r_ ?
#         result _   # list
#         __ _? ?
#             r__.ap.. ?
#
#         ___ i __ ra.. 1, le. ?
#             head _ ? |?
#             __ no. _ ? ?
#                 c..
#             tailPartition _ ? ? ?|
#             r__.e.. h.. + item ___ ? __ ?
#         r_ ?
#
#
# ? .? "aab"