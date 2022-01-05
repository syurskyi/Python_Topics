#!/usr/bin/python3
"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -. For each integer, you should choose one from +
and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target
S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
____ c.. _______ defaultdict


c_ Solution:
    ___ findTargetSumWays  A, S):
        """
        Let F[i][k] be number of ways for A[:i] sum to k
        F[i][k] = F[i-1][k-A[i-1]] + F[i-1][k+A[i-1]]

        :type A: List[int]
        :type S: int
        :rtype: int
        """
        __ n.. A:
            r..
        F = defaultdict(l....: defaultdict(i..))
        F[0][0] = 1
        ___ i __ r..(l..(A)):
            ___ k __ F[i].k..:  # F[i] for A[:i]
                F[i+1][k-A[i]] += F[i][k]
                F[i+1][k+A[i]] += F[i][k]

        r.. F[l..(A)][S]


__ _______ __ _______
    ... Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) __ 5
