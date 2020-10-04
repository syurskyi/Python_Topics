# # Longest Valid Parentheses
# # Question: Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# # For "(()", the longest valid parentheses substring is "()", which has length = 2.
# # Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
# # Solutions:
#
#
# c_ Solution
#     # @param s, a string
#     # @return an integer
#
#     ___ longestValidParentheses  s
#         maxlen stack last _ 0   # list, -1
#         ___ i __ ra.. le. s
#             __ ? ? __'('
#                 ?.ap.. ? # push the INDEX into the stack!!!!
#             ____
#                 __ ? __   # list:
#                     l.. _ ?
#                 ____
#                     ?.p..
#                     __ ? __   # list:
#                         m.. _ ma. ? ? - ?
#                     ____
#                         m.. _ ma. ? ? - ? le. ? - 1
#         r_ ?
#
#
# ? .? ")()())"