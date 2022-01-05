#!/usr/bin/python3
"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]


Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true


Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
"""
____ typing _______ List


c_ Solution:
    ___ validMountainArray  A: List[i..]) __ bool:
        """
        related to 845 Longest Mountain in Array

        use a flag
        """
        incr = 0  # 0 undecided, 1 increasing, 2 decresing
        ___ i __ r..(1, l..(A)):
            __ A[i] __ A[i-1]:
                r.. F..
            ____ A[i] > A[i-1]:
                __ incr __ 2:
                    r.. F..
                incr = 1
            ____:
                __ incr __ 0:
                    r.. F..
                incr = 2

        r.. incr __ 2
