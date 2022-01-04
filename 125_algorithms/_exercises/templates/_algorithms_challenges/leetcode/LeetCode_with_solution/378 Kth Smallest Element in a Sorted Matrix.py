"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in
the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 <= k <= n2.
"""
_______ heapq


__author__ = 'Daniel'


c_ Solution(object):
    ___ kthSmallest(self, matrix, k):
        """
        Heap of list
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = l..(matrix), l..(matrix[0])

        c_ Node(object):
            ___ - , i, j):
                i = i
                j = j

            ___ __cmp__(self, other):
                r.. matrix[i][j] - matrix[other.i][other.j]

            ___ hasnext
                r.. j+1 < n

            ___ next
                __ hasnext
                    r.. Node(i, j + 1)

                r.. StopIteration

        h    # list
        ___ i __ xrange(m):
            heapq.heappush(h, Node(i, 0))

        ret = N..
        ___ _ __ xrange(k):
            ret = heapq.heappop(h)
            __ ret.hasnext
                heapq.heappush(h, ret.next())

        r.. matrix[ret.i][ret.j]

    ___ kthSmallestError(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = l..(matrix), l..(matrix[0])
        i = k % n
        j = k - (i * m)
        r.. matrix[i][j]

__ _______ __ _______
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    print Solution().kthSmallest(matrix, k)
