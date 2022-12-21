# #! /usr/bin/env python
# # -*- coding: utf-8 -*-
#
#
# c.. Solution o..
#     ___ firstMissingPositive  nums
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # Put all i+1 in nums[i]
#         nums_len = l.. ?
#         ___ i __ r.. ?
#             # Swap nums[i] to the appropriate position until current
#             # nums[i] can't be push to the list, which is <0 or >nums_len
#             # By the way, pay attention to situation as [1,1].
#             _____ ? ? != ? + 1 a.. 0 < ? ? <_ ?
#                 index = ? ? - 1
#                 __ ? ? __ ? ?
#                     ______
#                 ?|?, ?|? = ?|? ? ?
#                 # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
#
#         ___ i __ r.. ?
#             __ ? ? != ? + 1:
#                 r_ ? + 1
#
#         r_ ? + 1
#
# """
# []
# [1,2,0]
# [3,4,-1,1]
# [3,4,-1,1,2,2,0,12,3]
# """
