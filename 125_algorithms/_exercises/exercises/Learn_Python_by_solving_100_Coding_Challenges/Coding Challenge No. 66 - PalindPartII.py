# # Palindrome Partitioning II
# # Question: Given a string s, partition s such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of s.
# # For example: given s = "aab", Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
# # Solutions:
#
#
# c_ Solution
#     # @param s, a string
#     # @return an integer
#
#     ___ partitionII  s
#         n _ le. s
#         f _   # list
#         p _ F.. ___ x __ ra.. ? ___ ? __ ra.. ?
#         #the worst case is cutting by each char
#         ___ i __ ra.. ? + 1
#             ?.ap.. ? - 1 - ? # the last one, f[n]=-1
#         ___ i __ r.. ra.. ?
#             ___ j __ ra.. ? ?
#                 __  ? ? __ ? ? an.  ? - ? < 2 o. ? ? + 1 ? - 1]
#                     ? ? ? _ T..
#                     ? ? _ mi. ? ? ? ? + 1 + 1
#         r_ ? 0
#
#
# ? .? "aab"