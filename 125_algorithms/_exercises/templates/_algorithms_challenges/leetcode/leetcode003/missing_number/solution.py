"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it
using only constant extra space complexity?
"""

class Solution(object
    ___ missingNumber(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        n = le.(nums)
        s = n * (n + 1) / 2
        res = 0
        ___ i in nums:
            res += i
        r_ s - res

s = Solution()
a1 = [0, 1, 3]
print(s.missingNumber(a1))
