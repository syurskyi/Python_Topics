# #! /usr/bin/env python
# # -*- coding: utf-8 -*-
#
#
# c.. Solution o..
#     ___ nextPermutation  nums
#         length _ l.. ?
#         index = ? - 1
#
#         """
#         Scan from the end of nums and get nums[index],
#         find one pair which nums[mark] > nums[mark - 1],
#         then swap the smallest number in nums[mark:] and nums[mark - 1].
#         Finally sort nums[mark:] and we will slove the problem.
#         """
#         _____ i.. >_ 1
#             __ ?|? > ?|? - 1
#                 ___ i __ r.. l.. - 1, ? - 1, -1
#                     __ ? ? > ?|? - 1
#                         ? ?, ?|? - 1] _ ?|? - 1 , ? ?
#                         ?|?| = s.. ?|?|
#                         r_
#             ____
#                 ? -_ 1
#
#         # Nums is in descending order, just reverse it.
#         ?.r..
#
# """
# []
# [1]
# [1,2,3]
# [3,2,1]
# [1,1,2,2,4,5,5]
# """
