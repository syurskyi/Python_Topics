# """
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and
# there exists one unique longest palindromic substring.
# """
# __author__ = 'Danyang'
#
#
# c_ Solution o..
#     ___ longestPalindrome  s
#         """
#         O(n^2)
#         :param s: string
#         :return: string
#         """
#         __ n.. ?
#             r..
#         n  l.. ?
#         __ ? __ 1
#             r.. ?
#
#         ret ? 0
#         ___ i __ x.. 0 ?
#             cur  g.. ? i i  # odd length
#             __ l.. ? > l.. ? r.. _ c..
#             cur = ? ? i ?+1
#             __ l.. ? > l.. ? r.. _ c..
#         r.. ?
#
#     ___ longestPalindrome_TLE  s
#         """
#         Algorithm: dp, O(n^2)
#
#         p[i,j] represents weather s[i:j] is palindrome. (incl. i-th while excl. j-th)
#         For example S = "abccb"
#                          01234
#         p[0,1] = True, p[1,2] = True, etc. since single char is Palindrom
#         p[0,2] = s[0]==s[1],
#         p[0,3] = s[0]==s[2] && p[1,2]
#         p[0,4] = s[0]==s[3] && p[1,3]
#         p[0,5] = s[0]==s[4] && p[1,4]
#
#         thus,
#         p[i,j] = 1 if i+1==j
#         p[i,j] = s[i]==s[j-1] if i+1==j-1 else
#         p[i,j] = s[i]==s[j-1] && p[i+1, j-1]
#
#         :param s: string
#         :return: string
#         """
#         length  l.. ?
#         dp  [.. ___ _ __ x.. ?+1 ___ _ __ x.. ? + 1
#         ___ i __ x.. ?+ 1
#             ? ? ? _ T..
#
#         longest  0, 0
#         ___ j __ x.. ? + 1
#             ___ i __ x.. ? - 1, -1, -1
#                 __ ?+1 __ ?
#                     ? ? ? _ T..
#                 ____
#                     ? ? ? _ ? ? __ ? ? - 1 a.. ? ? + 1 ? - 1  # pre-access? starting backward
#
#                 __ ? ? ? __ T.. a.. ? 1 - ? 0  < ?-?
#                     ? 0 ? 1 _ ? ?
#
#         r.. ? ? 0 | ? 1
#
#     ___ longestPalindrome_TLE2  s
#         """
#         :param s: string
#         :return: string
#         """
#         length  l.. ?
#
#         longest  ""
#         dp  F.. ___ _ __ x.. ?+1 ___ _ __ x.. ?+1  # larger than usual
#         ___ i __ x.. ?+1
#             ? ? ? _ T..  # empty
#         ___ i __ x.. ?
#             ? ? ? + 1 _ T..  # single char
#         ___ i __ x.. ?-1
#             ? ? ? + 2 _ ? ? __ ? ? + 1
#             __ ? ? ? + 1
#                 longest  ? i|?+2
#
#         ___ l __ x.. 3, ?+1  # breadth
#             ___ i __ x.. 0, ?-l
#                 __ ? ? __ ? ?+?-1
#                     ? ? ?+? _ ? ?+1 ?+?-1
#                 ____
#                     ? ? ?+? _ F..
#
#                 __ ? ? ?+? a.. l.. ? < ?
#                     longest  ? i:?+?
#
#         r.. ?
#
#     ___ get_palindrome_from_center  s begin end
#         """
#         # [begin, end]
#         """
#         w.... ? >_ 0 a.. ? < l.. ? a.. ? ? __ ? ?
#             b.. -_ 1
#             e.. +_ 1
#
#         r.. ? ? +1| >-1+1
#
#
# __ _______ __ _______
#     ... ?.l..("dfaaabbbaaac") __ "aaabbbaaa"