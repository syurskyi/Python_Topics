# """
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
# this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
# """
# __author__ = 'Danyang'
#
#
# c_ Solution
#     ___ convert  s nRows
#         """
#         Algorithm: matrix
#         :param s:
#         :param nRows:
#         :return: a String
#         """
#         length  l.. ?
#         matrix  || ___ _ __ x.. ?
#
#         i  0
#         w.... ? < ?
#             ___
#                 # going down
#                 ___ j __ x.. ?
#                     ? ?.a..? ?
#                     ? +_ 1
#
#                 # going up
#                 ___ j __ x.. ?-1-1, 0, -1
#                     ? ?.a.. ? ?
#                     ? +_ 1
#
#             ______ I..
#                 _____
#
#         lst  "".j.. element ___ ? __ ?
#         r.. "".j.. ?
#
#
# __ _______ __ _______
#     ... ?.c.. "ABCD", 2 __ "ACBD"