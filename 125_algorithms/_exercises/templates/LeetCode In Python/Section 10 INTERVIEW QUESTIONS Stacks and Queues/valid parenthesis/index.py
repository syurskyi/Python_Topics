# c_ Solution
#     ___ isEqual c1, c2  bo..
#         __ ? __ '(' a.. ? __ ')'
#             r_ T..
#         __ ? __ '[' a.. ? __ ']'
#             r_ T..
#         __ ? __ '{' a.. ? __ '}'
#             r_ T..
#         r_ F..
#
#     ___ isValid s st.  bo..
#         st _   # list
#         ___ character __ s
#             __ le. ? !_ 0
#                 li _ ? -1
#                 __ .i.. l. ?
#                     ?.p..
#                     c...
#             ?.ap.. ?
#         r_ le. ? __ 0
