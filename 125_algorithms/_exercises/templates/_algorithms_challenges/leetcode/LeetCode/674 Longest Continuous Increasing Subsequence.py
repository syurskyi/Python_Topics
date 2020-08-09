#!/usr/bin/python3
"""
Given an unsorted array of integers, find the length of longest continuous
increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its
length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous
one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length
is 1.
Note: Length of the array will not exceed 10,000.
"""
from typing ______ List


class Solution:
    ___ findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        pointer is sufficient
        """
        __ not nums:
            r_ 0

        ret = 1
        i = 1
        w___ i < le.(nums
            cur = 1
            w___ i < le.(nums) and nums[i] > nums[i-1]:
                cur += 1
                i += 1

            i += 1
            ret = max(ret, cur)

        r_ ret
