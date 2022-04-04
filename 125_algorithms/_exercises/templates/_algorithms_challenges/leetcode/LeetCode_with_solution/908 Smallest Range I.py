#!/usr/bin/python3
"""
Given an array A of integers, for each integer A[i] we may choose any x with
-K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the
minimum value of B.

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]


Note:
1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""
____ t___ _______ L..


c_ Solution:
    ___ smallestRangeI  A: L..[i..], K: i..) __ i..:
        """
        only need the max and min
        """
        r.. m..(0, m..(A) - K - (m..(A) + K
