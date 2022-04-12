"""
Main Concept:
just like found kth smallest num in matrix

example: [1, 2, 5, 7]

    7   5   2   1
1  1/7 1/5 1/2 1/1
2  2/7 2/5 ...
5  ...
7  ...
"""
____ h__ _______ heappush, heappop


c_ Solution:
    ___ kthSmallestPrimeFraction  A, K
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        heap    # list
        n l..(A)

        A.s..()

        ___ i __ r..(n
            heappush(heap, (A[i]/A[-1], i, n - 1

        ___ _ __ r..(K - 1
            _, i, j heappop(heap)

            j -_ 1
            __ j >_ 0:
                heappush(heap, (A[i]/A[j], i, j

        _, i, j heappop(heap)
        r.. [A[i], A[j]]
