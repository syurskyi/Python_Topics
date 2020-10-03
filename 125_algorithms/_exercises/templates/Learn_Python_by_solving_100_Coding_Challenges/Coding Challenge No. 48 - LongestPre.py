# # Longest common prefix
# # Question: Write a function to find the longest common prefix string amongst an array of strings.
# # For Example:
# # “Foo” and “Foobar” give “Foo” as longest prefix.
# # Solutions:
#
#
# c_ Solution
#     # @return a string
#     ___ longestCommonPrefix strs
#         __ le. ? __ 0
#             r_ ""
#         ___ i __ ra.. le. ? 0 -1 -1 -1
#             prefix _ ? 0 |? + 1
#             validPrefix _ T..
#             ___ j __ ra.. 1 le. ?
#                 __ le. ? ? <_ i o. ? ? |? + 1 !_ p..
#                     ? _ F..
#                     b..
#             __ ?
#                 r_ ?
#         r_ ""
#
#
# ? .? ["Foo","FooBar","Food"]