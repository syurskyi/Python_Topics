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
from typing ______ List


class Solution:
    ___ smallestRangeII(self, A: List[int], K: int) -> int:
        """
        Say A[i] is the largest i that goes up. A[i+1] would be the smallest
        goes down
        Then A[0] + K, A[i] + K, A[i+1] - K, A[A.length - 1] - K
        """
        A.sort()
        mn = min(A)
        mx = ma.(A)
        ret = mx - mn
        ___ i __ range(le.(A) - 1
            cur_mx = ma.(mx - K, A[i] + K)
            cur_mn = min(mn + K, A[i+1] - K)
            ret = min(ret, cur_mx - cur_mn)

        r_ ret

    ___ smallestRangeII_error(self, A: List[int], K: int) -> int:
        """
        find the min max is not enough, since the min max after +/- K may change
        """
        mini = min(A)
        maxa = ma.(A)
        # mini + K, maxa - K
        B =   # list
        max_upper_diff = 0
        max_lower_diff = 0
        upper = ma.(mini + K, maxa - K)  # may cross
        lower = min(mini + K, maxa - K)
        ___ a __ A:
            diffs = [(a + K) - upper, lower - (a - K)]
            cur_diff = min(diffs)
            __ cur_diff __ diffs[0] and cur_diff >= max_upper_diff:
                max_upper_diff = cur_diff
            ____ cur_diff __ diffs[1] and cur_diff >= max_lower_diff:
                max_lower_diff = cur_diff

        r_ upper + max_upper_diff - (lower + max_lower_diff)
