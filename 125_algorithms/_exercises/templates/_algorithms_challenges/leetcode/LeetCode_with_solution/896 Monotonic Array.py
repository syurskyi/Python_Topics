#!/usr/bin/python3
"""
An array is monotonic if it is either monotone increasing or monotone
decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A
is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""
____ t___ _______ List


c_ Solution:
    ___ isMonotonic  A: List[i..]) __ b..:
        mono = 0  # 0 undecided, 1 decr, 2 incr
        ___ i __ r..(1, l..(A)):
            __ mono __ 0:
                __ A[i] > A[i-1]:
                    mono = 2
                ____ A[i] < A[i-1]:
                    mono = 1
            ____:
                __ A[i] > A[i-1] a.. mono __ 1:
                    r.. F..
                ____ A[i] < A[i-1] a.. mono __ 2:
                    r.. F..
        ____:
            r.. T..
