"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into
another if and only if both the width and height of one envelope is greater than the width and height of the other
envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4]
=> [6,7]).
"""
_______ bisect

__author__ = 'Daniel'


class Solution(object):
    ___ maxEnvelopes(self, A):
        """
        LIS
        binary search

        sort by width first ascending, then sort by height descending (otherwise [3, 3] put in [3, 4]).
        :type A: List[List[int]]
        :rtype: int
        """
        __ n.. A: r.. 0

        A.s..(key=l.... (w, h): (w, -h))
        F = [-1 ___ _ __ xrange(l..(A)+1)]

        F[1] = A[0][1]  # store value rather than index
        k = 1
        ___ _, h __ A[1:]:
            idx = bisect.bisect_left(F, h, 1, k+1)
            F[idx] = h
            k += 1 __ idx __ k+1 ____ 0

        r.. k

    ___ maxEnvelopesTLE(self, A):
        """
        LIS
        O(n^2)
        :type A: List[List[int]]
        :rtype: int
        """
        __ n.. A: r.. 0

        predicate = l.... a, b: b[0] > a[0] a.. b[1] > a[1]
        A.s..()
        n = l..(A)
        F = [1 ___ _ __ xrange(n)]
        ___ i __ xrange(1, n):
            ___ j __ xrange(i):
                __ predicate(A[j], A[i]):
                    F[i] = max(F[i], 1 + F[j])

        r.. max(F)


__ __name__ __ "__main__":
    ... Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) __ 3
    ... Solution().maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]) __ 5
