# # Longest Palindromic Substring
# # Question: Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
# # Solutions:
#
#
# c_ Solution
#     # @param {string} s
#     # @return {string}
#
#     ___ longestPalindrome  s
#         l _ le. ?
#         __ ? <_ 2
#             __  ? 0 !_ ? ? - 1
#                 r_ ''
#             ____
#                 r_ ?
#         result _ ''
#         ___ i __ ra.. 0,l
#             palindrome _ ? ? ? ?
#             __ le. ? > le. ?
#                 r p
#             p.. _ ? ? ? ? + 1
#             __ le. p.. > le. r..
#                 ? _ ?
#         r_ ?
#
#     ___ SearchPalindrome  string start end
#         w___ ? >_ 0 an. ? < le. ? an. ? ? __ ? ?
#             ? -_ 1
#             ? +_ 1
#         r_ ? ? + 1|?
#
#
# ? .? "bananas"