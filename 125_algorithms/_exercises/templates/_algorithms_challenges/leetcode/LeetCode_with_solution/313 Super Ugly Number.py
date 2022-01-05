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
_______ heapq
____ c.. _______ d..
_______ sys

__author__ = 'Daniel'


c_ Solution(object):
    ___ nthSuperUglyNumber  n, primes):
        """
        DP O(kn)
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = l..(primes)
        ret = [sys.maxint ___ _ __ xrange(n)]
        ret[0] = 1
        # for each prime, a pointer pointing to the value of next unused number in the result
        idxes = [0 ___ _ __ xrange(k)]
        ___ i __ xrange(1, n):
            ___ j __ xrange(k):
                ret[i] = m..(ret[i], primes[j]*ret[idxes[j]])

            ___ j __ xrange(k):
                __ ret[i] __ primes[j]*ret[idxes[j]]:
                    idxes[j] += 1

        r.. ret[n-1]


c_ QueueWrapper(object):
    ___ - , idx, q):
        idx = idx
        q = q

    ___ __cmp__  other):
        r.. q[0] - other.q[0]


c_ SolutionHeap(object):
    ___ nthSuperUglyNumber  n, primes):
        """
        O(k lg k) + O(nk)
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ret = 1
        h = [QueueWrapper(i, d..([v])) ___ i, v __ e..(primes)]
        dic = {e.idx: e ___ e __ h}

        heapq.heapify(h)
        ___ _ __ xrange(n-1):
            mini = heapq.heappop(h)
            ret = mini.q.popleft()
            ___ i __ xrange(mini.idx, l..(primes)):
                dic[i].q.a..(ret*primes[i])
            heapq.heappush(h, mini)

        r.. ret

__ _______ __ _______
    ... Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]) __ 32