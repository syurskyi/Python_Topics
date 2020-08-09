# -*- coding: utf-8 -*-
"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For
example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes =
[2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
"""
______ heapq
from collections ______ deque
______ sys

__author__ = 'Daniel'


class Solution(object
    ___ nthSuperUglyNumber(self, n, primes
        """
        DP O(kn)
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = le.(primes)
        ret = [sys.maxint ___ _ in xrange(n)]
        ret[0] = 1
        # for each prime, a pointer pointing to the value of next unused number in the result
        idxes = [0 ___ _ in xrange(k)]
        ___ i in xrange(1, n
            ___ j in xrange(k
                ret[i] = min(ret[i], primes[j]*ret[idxes[j]])

            ___ j in xrange(k
                __ ret[i] __ primes[j]*ret[idxes[j]]:
                    idxes[j] += 1

        r_ ret[n-1]


class QueueWrapper(object
    ___ __init__(self, idx, q
        self.idx = idx
        self.q = q

    ___ __cmp__(self, other
        r_ self.q[0] - other.q[0]


class SolutionHeap(object
    ___ nthSuperUglyNumber(self, n, primes
        """
        O(k lg k) + O(nk)
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ret = 1
        h = [QueueWrapper(i, deque([v])) ___ i, v in enumerate(primes)]
        dic = {e.idx: e ___ e in h}

        heapq.heapify(h)
        ___ _ in xrange(n-1
            mini = heapq.heappop(h)
            ret = mini.q.popleft()
            ___ i in xrange(mini.idx, le.(primes)):
                dic[i].q.append(ret*primes[i])
            heapq.heappush(h, mini)

        r_ ret

__ __name__ __ "__main__":
    assert Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]) __ 32