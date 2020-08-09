#!/usr/bin/python3
"""
Given an unsorted array return whether an increasing subsequence of length 3
exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""
from typing ______ List
from bisect ______ bisect_left


class Solution:
    ___ increasingTriplet(self, nums: List[int]) -> bool:
        """
        Patience sort
        LIS dp with binary search
        """
        F = [float('inf') ___ _ in range(3)]
        ___ n in nums:
            i = bisect_left(F, n)
            __ i >= 2:
                r_ True
            F[i] = n

        r_ False
