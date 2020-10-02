# # Divide Two Integers
# # Question: Divide two integers without using multiplication, division and mod operator.
# # Solutions:
#
#
# c_ Solution
#     # @return an integer
#     ___ divide dividend, divisor
#         __  ? < 0 an. ? > 0 o.  ? > 0 an. ? < 0
#             __ ab. ? < ab. ?
#                 r_ 0
#         su. _ 0; count _ 0; res _ 0
#         a _ ab. ?; b _ ab. ?
#         w___ a >_ b
#             su. _ b
#             count _ 1
#             w___ su. + su. <_ a
#                 su. +_ su.
#                 c.. +_ c..
#             a -_ su.
#             res +_ c..
#         __  ? < 0 an. ? > 0 o.  ? > 0 an. ? < 0
#             r.. _ 0 - r..
#         r_ ?
#
#
# ?.? 100,5