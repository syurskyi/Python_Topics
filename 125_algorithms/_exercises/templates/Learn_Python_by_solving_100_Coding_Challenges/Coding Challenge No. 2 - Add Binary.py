# # Add Binary
# # Question: Given two binary strings, return their sum (also a binary string).
# # For example,
# # a = "11"
# # b = "1"
# # Return "100".
# # Solutions:
# c_ Solution
#     ___ addBinary  a b
#         length _ ma. le. ? le. ? + 1
#         su. _ '0' ___ i __ ra.. ?
#         __ le. ? <_ le. ?
#             ? _ '0' *   le. ? - le. ?  + ?
#         __ le. ? > le. ?
#             b _ '0' *   le. a - le. b  + b
#         Carry _ 0
#         i _ le. ? - 1
#         w___ i >_ 0
#             __ in. ? ? + in. ? ? + ? __ 3
#                 su. ? + 1 _ '1'
#                 ? _ 1
#             ____ in. ? ? + in. ? ? + ? __ 2
#                 su. ? + 1 _ '0'
#                 ? _ 1
#             ____ in. ? ? + in. ? ? + ? __ 1
#                 su. ? + 1 _ '1'
#                 ? _ 0
#             ____
#                 su. ? + 1 _ '0'
#                 ? _ 0
#             i _ ? - 1
#         __ ? __ 1
#             su. 0 _ '1'
#         __ ? __ 0
#             su. _ su. 1|?
#         su. _ ''.j.. su.
#         r_ su.
#
# ?.? "11" "1"
#
# c_ Solution
#     ___ addBinary a b
#         bia _ in. ? 2
#         bib _ in. ? 2
#         su. _ ? + ?
#         r_ st. "{0:b}".f.. su.
#
# ?.? "1" "11"
# # *Should only use if asked for shorter solution. It converts binary to integers; sum the integers. And finally formats the answer as binary.