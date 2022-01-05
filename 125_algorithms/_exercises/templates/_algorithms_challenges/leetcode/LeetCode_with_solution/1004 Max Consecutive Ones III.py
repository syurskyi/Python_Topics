#!/usr/bin/python3
"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.



Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


Note:
1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1
"""
____ typing _______ List


c_ Solution:
    ___ longestOnes  A: List[i..], K: i..) __ i..:
        """
        len(gap)
        But there is multiple gap need to fill, and which gaps to fill is
        undecided. Greedy? No. DP?

        Sliding Window: Find the longest subarray with at most K zeros.
        """
        i, j = 0, 0
        cnt_0 = 0
        n = l..(A)
        ret = 0
        w.... i < n a.. j < n:
            w.... j < n:
                __ A[j] __ 0 a.. cnt_0 < K:
                    j += 1
                    cnt_0 += 1
                ____ A[j] __ 1:
                    j += 1
                ____:
                    _____

            ret = m..(ret, j - i)
            __ A[i] __ 0:
                cnt_0 -= 1
            i += 1

        r.. ret


__ _______ __ _______
    ... Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) __ 6
