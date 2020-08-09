"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
"""
______ heapq


__author__ = 'Daniel'


class Node(object
    """
    Data structure is key
    """
    ___ __init__(self, origin, q
        self.origin = origin
        self.q = q

    ___ __cmp__(self, other
        r_ self.q[0] - other.q[0]


class Solution(object
    ___ nthUglyNumber(self, n
        """
        Prime factor: 2, 3, 5
        Heap
        :type n: int
        :rtype: int
        """
        __ n __ 1:
            r_ 1

        n -= 1  # exclude 1

        ugly = [2, 3, 5]
        qs = [Node(i, [i]) for i in ugly]
        h = list(qs)  # shallow copy

        heapq.heapify(h)

        cnt = 0
        ret = 2
        w___ cnt < n:
            cnt += 1
            popped = heapq.heappop(h)
            ret = popped.q.pop(0)
            for i in xrange(ugly.index(popped.origin), 3
                qs[i].q.append(ret*ugly[i])

            heapq.heappush(h, popped)

        r_ ret


__ __name__ __ "__main__":
    assert Solution().nthUglyNumber(10) __ 12
