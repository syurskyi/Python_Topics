#!/usr/bin/python3
"""
Given an array of integers and an integer k, you need to find the total
number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer
k is [-1e7, 1e7].
"""
____ typing _______ List
____ collections _______ defaultdict


c_ Solution:
    ___ subarraySum(self, nums: List[i..], k: i..) __ i..:
        """
        prefix sum
        """
        h = defaultdict(i..)
        ret = 0
        s = 0
        h[s] += 1
        ___ n __ nums:
            s += n
            ret += h[s - k]
            h[s] += 1

        r.. ret
