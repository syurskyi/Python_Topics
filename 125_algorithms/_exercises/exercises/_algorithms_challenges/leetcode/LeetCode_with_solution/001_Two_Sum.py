# c_ Solution o..
#     # def twoSum(self, nums, target):
#     #     """
#     #     :type nums: List[int]
#     #     :type target: int
#     #     :rtype: List[int]
#     #     """
#     #     #n^2
#     #     ls = len(nums)
#     #     for i in range(ls):
#     #         for j in range(i + 1, ls):
#     #             if nums[i] + nums[j] == target:
#     #                 return [i, j]
#
#     # def twoSum(self, nums, target):
#     #     # hash 1
#     #     hash_nums = {}
#     #     for index, num in enumerate(nums):
#     #         try:
#     #             hash_nums[num].append(index)
#     #         except KeyError:
#     #             hash_nums[num] = [index]
#     #     for index, num in enumerate(nums):
#     #         another = target - num
#     #         try:
#     #             candicate = hash_nums[another]
#     #             if another == num:
#     #                 if len(candicate) > 1:
#     #                     return candicate
#     #                 else:
#     #                     continue
#     #             else:
#     #                 return [index, candicate[0]]
#     #         except KeyError:
#     #             pass
#
#     # def twoSum(self, nums, target):
#     #     # hash 2
#     #     hash_nums = {}
#     #     for index, num in enumerate(nums):
#     #         another = target - num
#     #         try:
#     #             hash_nums[another]
#     #             return [hash_nums[another], index]
#     #         except KeyError:
#     #             hash_nums[num] = index
#
#     ___ twoSum  nums target
#         # two point
#         nums_index  v index ___ ? ? __ e.. ?
#         ?.s..
#         begin end  0, l.. ? - 1
#         w.. ? < ?
#             curr  ? ? 0 + ? ? 0
#             __ ? __ t..
#                 r_ ? ? 1 ? ?1
#             ____ c.. < ?
#                 ? +_ 1
#             ____
#                 ? -_ 1
#
#
# __ ____ __ ____
#     # begin
#     s  ?
#     print ?.t.. ([3, 2, 4], 6)
