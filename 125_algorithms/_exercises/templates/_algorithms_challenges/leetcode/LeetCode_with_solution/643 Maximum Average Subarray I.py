#!/usr/bin/python3
"""
Given an array consisting of n integers, find the contiguous subarray of given
length k that has the maximum average value. And you need to output the maximum
average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75


Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""
____ t___ _______ L..


c_ Solution:
    ___ findMaxAverage  nums: L..[i..], k: i..) __ f__:
        """
        two pointers
        """
        cur_sum = s..(nums[:k])
        maxa = cur_sum
        i = k
        w.... i < l..(nums
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            maxa = m..(maxa, cur_sum)
            i += 1

        r.. maxa / k
