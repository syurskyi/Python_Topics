# -*- coding: utf-8 -*-
"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are
asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here
left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
__author__ = 'Daniel'


c_ Solution(o..
    ___ maxCoins  A
        """
        Divide & Conquer <- Divide Boundary <- Reverse Thinking

        Let F[i][j] be the max scores burst all over A[i:j]
        F[i][j] = max(F[i][k] + A[i-1]*A[k]*A[j] + F[k+1][j] \forall k) where k is the last one to burst.

        Reference: https://leetcode.com/discuss/72216/share-some-analysis-and-explanations?show=72358#c72358
        :type A: List[int]
        :rtype: int
        """
        n = l..(A)

        ___ g.. i
            __ i < 0 o. i >= n: r.. 1
            r.. A[i]

        F = [[0 ___ _ __ x..(n+1)] ___ _ __ x..(n+1)]
        ___ i __ x..(n+1, -1, -1
            ___ j __ x..(i+1, n+1
                F[i][j] = m..(
                    F[i][k]+g.. i-1)*g.. k)*g.. j)+F[k+1][j]
                    ___ k __ x..(i, j)
                )

        r.. m.. m..(m.., F))


__ _______ __ _______
    ... Solution().maxCoins([3, 1, 5, 8]) __ 167

