# # ZigZag Conversion
# # Question: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# # P A H N
# # A P L S I I G
# # Y I R
# # And then read line by line: "PAHNAPLSIIGYIR"
# # Write the code that will take a string and make this conversion given a number of rows:
# # string convert(string text, int nRows);
# # convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
# # Solutions:
#
#
# ______ f..
# ______ o..
#
# c_ Solution
#     # @param {string} s
#     # @param {integer} numRows
#     # @return {string}
#     ___ convert  s numRows
#         __ ? __ 1 o. ? >_ le. ?
#             r_ ?
#         zigzag _  ___ x __ ra.. ?
#         row, step _ 0 1
#         ___ c __ s
#             z.. r.. +_ ?
#             __ ? __ 0
#                 s.. _ 1
#             ____ ? __ ? - 1
#                 s.. _ -1
#             r.. +_ s..
#         r_ ''.j.. f__.r.. o__.a.. ?
#
#
# ? .? "PAYPALISHIRING" 3