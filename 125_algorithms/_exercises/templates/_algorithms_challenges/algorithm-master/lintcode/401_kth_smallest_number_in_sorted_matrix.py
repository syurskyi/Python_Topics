_______ h__

c_ Solution:
    """
    @param: matrix: a matrix of integers
    @param: k: An integer
    @return: the kth smallest number in the matrix
    """
    ___ kthSmallest  matrix, k
        ans j 0
        heap, m, n    # list, l..(matrix), l..(matrix[0])
        ___ i __ r..(m..(k, m: h__.heappush(heap, (matrix[i][0], i, 0
        w.... k > 0:
            ans h__.heappop(heap)
            j ans[2] + 1
            __ j < n:
                h__.heappush(heap, (matrix[ans[1]][j], ans[1], j
            k -_ 1
        r.. ans[0]
