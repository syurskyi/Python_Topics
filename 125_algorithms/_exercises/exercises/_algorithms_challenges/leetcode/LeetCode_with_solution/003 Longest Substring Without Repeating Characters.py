# """
# Given a string, find the length of the longest substring without repeating characters. For example, the longest
# substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
# is "b", with the length of 1.
# """
# __author__ = 'Danyang'
#
#
# c_ Solution
#     ___ lengthOfLongestSubstring  s
#         """
#         Algorithm: Hash Map, two pointers
#         Hash Map: array visited = [] for all ascii, notice the algorithm of updating this array
#         Two pointers: start - start of the string; ind - scanning
#
#         Given a string, find the length of the longest substring without repeating characters.
#         :param s: String
#         :return: Integer
#         """
#         # last visited index in the string
#         visited_last_index  -1 ___ _ __ r.. 256  # ascii
#         longest  0  # record result
#
#         start  0  # pointer
#         ___ ind val __ e.. ?
#             __ ? o.. ? __ -1
#                 longest  m.. ?  i.. -s..+1
#             ____
#                 longest  m.. ? i..-1 -s..+1
#
#                 # unmark
#                 ___ i __ r.. s.. ? o.. ?
#                     ? o.. ? ? = -1
#
#                 start  ? o.. ? +1
#
#             ? o.. ?  i..  # update last visited index
#
#         r.. ?

# __ _____ __ _____
#     s ?
#     answer  ?.l.. "fivestarview"
#     print ?