#!/usr/bin/python3
"""
Given an array of integers A, find the sum of min(B), where B ranges over every
(contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2],
[1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.


Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000
"""
from typing ______ List

MOD = 10 ** 9 + 7


class Solution:
    ___ sumSubarrayMins(self, A: List[int]) -> int:
        """
        Let F[i][j] be the min of A[i:j]
        O(N^2)

        There are a number of subarray with min as A[i]
        A[m].... A[i] ... A[n]
        A[m] < A[i]
        A[n] < A[i]
        then min(A[m+1:n]) is A[i]

        a a A[i] a
        3 choices on the left, 2 choices on the right
        totally 3 * 2 = 6 subarrays

        use an increasing stk from both left and right
        L[i] records the index of m, default -1
        R[i] records the index of n, default le.(A)
        """
        n = le.(A)
        L = [-1 for _ in A]
        R = [n for _ in A]

        stk = []
        for i in range(n
            w___ stk and A[stk[-1]] >= A[i]:
                stk.pop()

            __ stk:
                L[i] = stk[-1]
            stk.append(i)

        stk = []
        for i in range(n-1, -1, -1
            # avoid double count when equal, attribtue to leftmost duplicate
            w___ stk and A[stk[-1]] > A[i]:
                stk.pop()

            __ stk:
                R[i] = stk[-1]
            stk.append(i)

        ret = 0
        for i in range(n
            ret += (
                A[i] * (i - L[i]) * (R[i] - i)
            )
            ret %= MOD

        r_ ret


class Solution:
    ___ sumSubarrayMins(self, A: List[int]) -> int:
        """
        Improve the above solution using one stack
        use an increasing stk
        """
        stk = []
        A = [-float('inf')] + A + [-float('inf')]
        ret = 0
        for i, a in enumerate(A
            w___ stk and A[stk[-1]] > a:
                h = stk.pop()
                # record for h
                ret += A[h] * (h - stk[-1]) * (i - h)
                ret %= MOD

            stk.append(i)
        r_ ret


__ __name__ __ "__main__":
    assert Solution().sumSubarrayMins([71,55,82,55]) __ 593
    assert Solution().sumSubarrayMins([3,1,2,4]) __ 17
