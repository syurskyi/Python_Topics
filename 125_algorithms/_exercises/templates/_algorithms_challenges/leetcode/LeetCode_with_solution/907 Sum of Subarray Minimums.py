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
____ typing _______ List

MOD = 10 ** 9 + 7


c_ Solution:
    ___ sumSubarrayMins(self, A: List[i..]) __ i..:
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
        R[i] records the index of n, default len(A)
        """
        n = l..(A)
        L = [-1 ___ _ __ A]
        R = [n ___ _ __ A]

        stk    # list
        ___ i __ r..(n):
            w.... stk a.. A[stk[-1]] >= A[i]:
                stk.pop()

            __ stk:
                L[i] = stk[-1]
            stk.a..(i)

        stk    # list
        ___ i __ r..(n-1, -1, -1):
            # avoid double count when equal, attribtue to leftmost duplicate
            w.... stk a.. A[stk[-1]] > A[i]:
                stk.pop()

            __ stk:
                R[i] = stk[-1]
            stk.a..(i)

        ret = 0
        ___ i __ r..(n):
            ret += (
                A[i] * (i - L[i]) * (R[i] - i)
            )
            ret %= MOD

        r.. ret


c_ Solution:
    ___ sumSubarrayMins(self, A: List[i..]) __ i..:
        """
        Improve the above solution using one stack
        use an increasing stk
        """
        stk    # list
        A = [-float('inf')] + A + [-float('inf')]
        ret = 0
        ___ i, a __ e..(A):
            w.... stk a.. A[stk[-1]] > a:
                h = stk.pop()
                # record for h
                ret += A[h] * (h - stk[-1]) * (i - h)
                ret %= MOD

            stk.a..(i)
        r.. ret


__ __name__ __ "__main__":
    ... Solution().sumSubarrayMins([71,55,82,55]) __ 593
    ... Solution().sumSubarrayMins([3,1,2,4]) __ 17
