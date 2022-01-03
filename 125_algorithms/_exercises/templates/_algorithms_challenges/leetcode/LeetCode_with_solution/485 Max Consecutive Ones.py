#!/usr/bin/python3
"""
Given a binary array, find the maximum number of consecutive 1s in this array.
"""


c_ Solution:
    ___ findMaxConsecutiveOnes(self, nums):
        """
        two pointers
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        e = 0
        ret = 0
        w.... s < l..(nums):
            __ nums[s] __ 1:
                w.... e < l..(nums) a.. nums[e] __ 1:
                    e += 1
                ret = max(ret, e - s)
            ____:
                e += 1

            s = e

        r.. ret


__ __name__ __ "__main__":
    ... Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]) __ 3
