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
____ t___ _______ L..


# Definition for an interval.
c_ Interval:
    ___ - , s=0, e=0
        start s
        end e


c_ Solution:
    ___ intervalIntersection  A: L..[Interval], B: L..[Interval]) __ L..[Interval]:
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
        i, j 0, 0
        m, n l..(A), l..(B)
        ret    # list
        w.... i < m a.. j < n:
            lo m..(A[i].start, B[j].start)
            hi m..(A[i].end, B[j].end)
            __ lo <_ hi:
                ret.a..(Interval(lo, hi
            __ A[i].end > B[j].end:
                j += 1
            ____
                i += 1

        r.. ret

    ___ intervalIntersection_complex  A: L..[Interval], B: L..[Interval]) __ L..[Interval]:
        """
        like merge
        """
        ret    # list
        i 0
        j 0
        m, n l..(A), l..(B)
        w.... i < m a.. j < n:
            a A[i]
            b B[j]
            __ b.start <_ a.end <_ b.end:
                ret.a..(Interval(m..(a.start, b.start), a.end
                i += 1
            ____ a.start <_ b.end <_ a.end:
                ret.a..(Interval(m..(a.start, b.start), b.end
                j += 1
            ____
                __ a.end < b.start:
                    i += 1
                ____
                    j += 1
        r.. ret
