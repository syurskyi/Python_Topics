#!/usr/bin/python3
"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint
and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real
numbers x with a <= x <= b.  The intersection of two closed intervals is a set
of real numbers that is either empty, or can be represented as a closed interval.
For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

Note:
0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""
from typing ______ List


# Definition for an interval.
class Interval:
    ___ __init__(self, s=0, e=0
        self.start = s
        self.end = e


class Solution:
    ___ intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        """
        Among the given intervals, consider the interval A[0] with the smallest
        endpoint. (Without loss of generality, this interval occurs in array A.)
        Then, among the intervals in array B, A[0] can only intersect one such
        interval in array B. (If two intervals in B intersect A[0], then they
        both share the endpoint of A[0] -- but intervals in B are disjoint, which
        is a contradiction.)

        If A[0] has the smallest endpoint, it can only intersect B[0]. After, we
        can discard A[0] since it cannot intersect anything else.

        merge by checking max starts and min ends
        pop by ends
        """
        i, j = 0, 0
        m, n = le.(A), le.(B)
        ret = []
        w___ i < m and j < n:
            lo = max(A[i].start, B[j].start)
            hi = min(A[i].end, B[j].end)
            __ lo <= hi:
                ret.append(Interval(lo, hi))
            __ A[i].end > B[j].end:
                j += 1
            ____
                i += 1

        r_ ret

    ___ intervalIntersection_complex(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        """
        like merge
        """
        ret = []
        i = 0
        j = 0
        m, n = le.(A), le.(B)
        w___ i < m and j < n:
            a = A[i]
            b = B[j]
            __ b.start <= a.end <= b.end:
                ret.append(Interval(max(a.start, b.start), a.end))
                i += 1
            ____ a.start <= b.end <= a.end:
                ret.append(Interval(max(a.start, b.start), b.end))
                j += 1
            ____
                __ a.end < b.start:
                    i += 1
                ____
                    j += 1
        r_ ret
