# c_ Solution
#
#     ___ backtracking ans m digits combination index
#         __ i.. > le. d..
#             r_
#         __ le. c.. __ le. d..
#             a__.ap.. c.. |
#             r_
#
#         currentDigit _ d.. i..
#         curString _ m c..
#
#         ___ i __ ra.. le. curString
#             .b.. ? ? ? ? +
#                               c.. ? i.. + 1
#
#     ___ letterCombinations digits st.  L.. st.
#         ans _   # list
#         __ le. ? __ 0
#             r_ ?
#
#         m _   # dict
#
#         m['2'] _ "abc"
#         m['3'] _ "___"
#         m['4'] _ "ghi"
#         m['5'] _ "jkl"
#         m['6'] _ "mno"
#         m['7'] _ "pqrs"
#         m['8'] _ "tuv"
#         m['9'] _ "wxyz"
#
#         .b.. ? ? ? "" 0
#
#         r_ ?
