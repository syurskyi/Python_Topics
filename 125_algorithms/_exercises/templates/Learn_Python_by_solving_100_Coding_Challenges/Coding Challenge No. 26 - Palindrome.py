# # Palindrome
# # Question: Checking whether or not a string is a palindrome. It spells the same forward as backwards. Write a method to determine if a string is a palindrome
# # Note: remove any extraneous things like spaces or punctuation from the string. So the following strings would all be palindromes. "racecar", "race car" "race, car ".
# # Solutions:
#
#
# c_ Solution
#     # @param s, a string
#     # @return a boolean
#     ___ isPalindrome s
#         __ le. ? < 2
#             r_ T..
#         head tail _ 0, le. ? - 1
#         w___ ? < ?
#             __ no. ? ?.isa..
#                 ? +_ 1
#             ____ no. ? ? .isa..
#                 ? -_ 1
#             ____
#                 __ ? ?.l.. __ ? ?.l..
#                     ? +_ 1
#                     ? -_ 1
#                 ____
#                     r_ F..
#         r_ T..
#
#
# ? .? ["racecar","race car","race, car"]