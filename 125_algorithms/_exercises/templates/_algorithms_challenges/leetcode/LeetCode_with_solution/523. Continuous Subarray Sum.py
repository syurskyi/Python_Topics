#!/usr/bin/python3
"""
Given a list of non-negative numbers and a target integer k, write a function to
check if the array has a continuous subarray of size at least 2 that sums up to
the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
 sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit
integer.
"""


c_ Solution:
    ___ checkSubarraySum(self, nums, k):
        """
        Two pointers algorithm won't work since it is multiple of k

        prefix sum + hashmap (look back) + mod k (Math)
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        h = {0: 0}  # [:l], half open, factor in trival case
        s = 0
        ___ l __ r..(1, l..(nums) + 1):
            s += nums[l-1]
            __ k != 0:  # edge case
                s %= k
            __ s __ h:
                __ l - h[s] >= 2:  # size at least 2
                    r.. T..
            ____:
                # only keep the lowest
                h[s] = l

        r.. F..


__ __name__ __ "__main__":
    ... Solution().checkSubarraySum([23,2,4,6,7], 6) __ T..
