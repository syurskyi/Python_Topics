#!/usr/bin/python3
"""
Given a binary array, find the maximum number of consecutive 1s in this array.
"""


class Solution:
    ___ findMaxConsecutiveOnes(self, nums
        """
        two pointers
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        e = 0
        ret = 0
        w___ s < le.(nums
            __ nums[s] __ 1:
                w___ e < le.(nums) and nums[e] __ 1:
                    e += 1
                ret = max(ret, e - s)
            ____
                e += 1

            s = e

        r_ ret


__ __name__ __ "__main__":
    assert Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]) __ 3
