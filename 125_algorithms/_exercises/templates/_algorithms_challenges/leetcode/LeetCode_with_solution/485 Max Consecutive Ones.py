#!/usr/bin/python3
"""
Given a binary array, find the maximum number of consecutive 1s in this array.
"""


class Solution:
    ___ findMaxConsecutiveOnes(self, nums):
        """
        two pointers
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        e = 0
        ret = 0
        while s < len(nums):
            __ nums[s] == 1:
                while e < len(nums) and nums[e] == 1:
                    e += 1
                ret = max(ret, e - s)
            else:
                e += 1

            s = e

        return ret


__ __name__ == "__main__":
    assert Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
