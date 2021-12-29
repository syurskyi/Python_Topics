#!/usr/bin/python3
"""
Given an array A of integers, for each integer A[i] we need to choose either
x = -K or x = K, and add x to A[i] (only once).

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
Output: 3
Explanation: B = [4,6,3]

Note:
1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""
____ typing _______ List


class Solution:
    ___ smallestRangeII(self, A: List[int], K: int) -> int:
        """
        Say A[i] is the largest i that goes up. A[i+1] would be the smallest
        goes down
        Then A[0] + K, A[i] + K, A[i+1] - K, A[A.length - 1] - K
        """
        A.s..()
        mn = m..(A)
        mx = max(A)
        ret = mx - mn
        ___ i __ r..(l..(A) - 1):
            cur_mx = max(mx - K, A[i] + K)
            cur_mn = m..(mn + K, A[i+1] - K)
            ret = m..(ret, cur_mx - cur_mn)

        r.. ret

    ___ smallestRangeII_error(self, A: List[int], K: int) -> int:
        """
        find the min max is not enough, since the min max after +/- K may change
        """
        mini = m..(A)
        maxa = max(A)
        # mini + K, maxa - K
        B    # list
        max_upper_diff = 0
        max_lower_diff = 0
        upper = max(mini + K, maxa - K)  # may cross
        lower = m..(mini + K, maxa - K)
        ___ a __ A:
            diffs = [(a + K) - upper, lower - (a - K)]
            cur_diff = m..(diffs)
            __ cur_diff __ diffs[0] a.. cur_diff >= max_upper_diff:
                max_upper_diff = cur_diff
            ____ cur_diff __ diffs[1] a.. cur_diff >= max_lower_diff:
                max_lower_diff = cur_diff

        r.. upper + max_upper_diff - (lower + max_lower_diff)
