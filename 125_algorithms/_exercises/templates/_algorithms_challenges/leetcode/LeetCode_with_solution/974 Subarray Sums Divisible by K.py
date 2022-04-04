#!/usr/bin/python3
"""
Given an array A of integers, return the number of (contiguous, non-empty)
subarrays that have a sum divisible by K.

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""
____ t___ _______ List
____ c.. _______ d..


c_ Solution:
    ___ subarraysDivByK_2  A: List[i..], K: i..) __ i..:
        """
        count the prefix sum mod K
        nC2
        """
        prefix_sum = 0
        counter = d..(i..)
        counter[0] = 1  # important trival case
        ___ a __ A:
            prefix_sum += a
            prefix_sum %= K
            counter[prefix_sum] += 1

        ret = 0
        ___ v __ counter.v..
            ret += v * (v-1) // 2

        r.. ret

    ___ subarraysDivByK  A: List[i..], K: i..) __ i..:
        """
        Prefix sum
        O(N^2)
        How to optimize?
        Mapping to prefix sum to count
        Divide: Translate divisible by K into mod.
        prefix sum has to be MOD by K.
        """
        prefix_sum = 0
        counter = d..(i..)
        counter[0] = 1  # trival case. !important
        ret = 0
        ___ a __ A:
            prefix_sum += a
            prefix_sum %= K
            ret += counter[prefix_sum]  # count of previously matching prefix sum
            counter[prefix_sum] += 1

        r.. ret
