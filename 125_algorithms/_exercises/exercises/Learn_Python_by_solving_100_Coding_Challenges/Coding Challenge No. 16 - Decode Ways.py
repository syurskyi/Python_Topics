# # Decode Ways
# # Question: A message containing letters from A-Z is being encoded to numbers using the following mapping:
# # 'A' -> 1
# # 'B' -> 2
# # ...
# # 'Z' -> 26
# # Given an encoded message containing digits, determine the total number of ways to decode it.
# # For example:
# # Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
# # The number of ways decoding "12" is 2.
# # Solutions:
#
#
# c_ Solution
#     # @param s is a string
#     # @return an integer
#     ___ numDecodings s
#         __ ?__"" o. ? 0__'0': r_ 0
#         dp_[1,1]
#         ___ i __ ra.. 2, le. ? + 1
#             __ 10 <_ in. ? ?-2|? <_26 an. ? ? - 1 !_ '0'
#                 ?.ap.. ? ? - 1 + ? ? - 2
#             ____ in. ? ? - 2|? __10 o. in. ? ? - 2|? __20
#                 ?.ap.. ? ? - 2
#             ____ ? ? - 1 !_ '0'
#                 ?.ap.. ? ? - 1
#             ____
#                 r_ 0
#         r_ ? le. ?
#
# ?.? "12"