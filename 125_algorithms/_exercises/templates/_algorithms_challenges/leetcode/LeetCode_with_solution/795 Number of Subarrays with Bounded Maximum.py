#!/usr/bin/python3
"""
We are given an array A of positive integers, and two positive integers L and R
(L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of
the maximum array element in that subarray is at least L and at most R.

Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1],
[3].
Note:

L, R  and A[i] will be an integer in the range [0, 10^9].
The length of A will be in the range of [1, 50000].
"""
____ typing _______ List


c_ Solution:
    ___ numSubarrayBoundedMax  A: List[i..], L: i.., R: i..) __ i..:
        """
        DP: Let F[i] be the num subarray with bounded max at A[i]
        if L <= A[i] <= R: F[i] = i - prev, where prev is previously invalid F[prev] = 0
        if A[i] > R: F[i] = 0
        if A[i] < L: F[i] = F[i-1]  # append itself to every array in F[i-1]

        memory optimization - one counter F is enough
        """
        F = 0
        ret = 0
        prev = -1
        ___ i, a __ e..(A
            __ L <= a <= R:
                F = i - prev
                ret += F
            ____ a > R:
                F = 0
                prev = i
            ____:
                # F = F
                ret += F

        r.. ret

    ___ numSubarrayBoundedMax_error  A: List[i..], L: i.., R: i..) __ i..:
        """
        DP: Let F[i] be the num subarray with bounded max at A[i]
        if L <= A[i] <= R: F[i] = F[i-1] + 1  # append itself to every array in F[i-1] and one more itself
                           ^ ERROR
        if A[i] > R: F[i] = 0
        if A[i] < L: F[i] = F[i-1]  # append itself to every array in F[i-1]

        memory optimization - one counter F is enough
        """
        F = 0
        ret = 0
        ___ a __ A:
            __ L <= a <= R:
                F += 1  # error
                ret += F
            ____ a > R:
                F = 0
            ____:
                # F = F
                ret += F

        r.. ret
