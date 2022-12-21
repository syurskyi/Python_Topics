# class Solution(object):
#     def findPeakElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

c_ Solution o..
    ___ findPeakElement  nums
        # https://leetcode.com/discuss/88467/tricky-problem-tricky-solution
        # note that num[-1] = num[n] = -∞
        start, end = 0, l.. nums) - 1
        w.. start < end:
            mid = (start + end) / 2
            __ nums[mid] < nums[mid+1]:
                start= mid + 1
            ____
                end = mid
        r_ start
