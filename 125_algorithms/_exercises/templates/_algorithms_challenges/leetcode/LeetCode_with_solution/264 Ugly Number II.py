"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
"""
_______ heapq


__author__ 'Daniel'


c_ Node(o..
    """
    Data structure is key
    """
    ___ - , origin, q
        origin origin
        q q

    ___ __cmp__  other
        r.. q[0] - other.q[0]


c_ Solution(o..
    ___ nthUglyNumber  n
        """
        Prime factor: 2, 3, 5
        Heap
        :type n: int
        :rtype: int
        """
        __ n __ 1:
            r.. 1

        n -_ 1  # exclude 1

        ugly [2, 3, 5]
        qs [Node(i, [i]) ___ i __ ugly]
        h l..(qs)  # shallow copy

        heapq.heapify(h)

        cnt 0
        ret 2
        w.... cnt < n:
            cnt += 1
            popped heapq.heappop(h)
            ret popped.q.p.. 0)
            ___ i __ x..(ugly.i.. popped.origin), 3
                qs[i].q.a..(ret*ugly[i])

            heapq.heappush(h, popped)

        r.. ret


__ _______ __ _______
    ... Solution().nthUglyNumber(10) __ 12
