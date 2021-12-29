# # Generate Parentheses
# # Question: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# # For example, given n = 3, a solution set is:
# # "((()))", "(()())", "(())()", "()(())", "()()()"
# # Solutions:
#
# c_ Solution
#     # @param an integer
#     # @return a list of string
#     ___ helpler  l r item res
#         __ ? < ?
#             r_
#         __ ? __ 0 an. r __ 0
#             r__.ap.. i..
#         __ ? > 0
#             ? l - 1 ? i.. + '(' r..
#         __ ? > 0
#             ? ? ? - 1 i.. + ')' r..
#
#     ___ generateParenthesis n
#         __ ? __ 0
#             r_   # list
#         res _   # list
#         ? ? n '' r..
#         r_ ?
#
#
# ? .? 3