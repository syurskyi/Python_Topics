# """
# Given an array of integers, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be
# less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
# """
# __author__ = 'Danyang'
#
#
# c_ Solution
#     ___ twoSum_TLE  num target
#         """
#         built-in method .index
#         :param num: list
#         :param target: int
#         :return: tuple, (index1, index2)
#         """
#         nums ?
#         ___ ind1, val __ e.. ?
#             ___
#                 ind2  ?.i.. t.. - v..
#                 r.. ind1+1, ind2+1
#             ______ V..
#                 _____
#
#     ___ twoSum_TLE_2  num, target
#         nums ?
#         ___ ind1, val __ e.. ?
#             __ t..-v.. __ ?
#                 r.. ind1+1, ?.i.. t..-v.. +1
#
#     ___ twoSum  num target
#         """
#         Hash Map
#
#         :param num: list
#         :param target: int
#         :return: tuple, (index1, index2)
#         """
#         hash_map    # dict
#         ___ ind val __ e.. ?
#             ? ?  ?
#
#         ___ ind1 val __ e.. ?
#             __ t..-v.. __ ?
#                 ind2  ? t..-v..
#                 __ __1!_ ?
#                     r.. __1+1, ?+1
#
#
# __ _____ __ ____
#     print ?.t.. 3, 2, 4], 6