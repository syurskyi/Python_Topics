"""
Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(x1, y1, x2, y2)
"""


c_ NumMatrix:
    ___ - , matrix
        """
        :type matrix: List[List[int]]
        """
        __ n.. matrix o. n.. matrix[0]:
            r..

        m, n = l..(matrix), l..(matrix[0])
        prefix_sum = [[0] * (n + 1) ___ _ __ r..(m + 1)]

        ___ x __ r..(1, m + 1
            ___ y __ r..(1, n + 1
                prefix_sum[x][y] = s..((
                    prefix_sum[x - 1][y],
                    prefix_sum[x][y - 1],
                    - prefix_sum[x - 1][y - 1],
                    matrix[x - 1][y - 1],


    ___ sumRegion  x1, y1, x2, y2
        """
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: int
        """
        __ n.. a..((
            prefix_sum,
            prefix_sum[0],
            0 <_ x1 < l..(prefix_sum),
            0 <_ x2 + 1 < l..(prefix_sum),
            0 <_ y1 < l..(prefix_sum[0]),
            0 <_ y2 + 1 < l..(prefix_sum[0]),
        :
            r.. 0

        r.. s..((
            prefix_sum[x2 + 1][y2 + 1],
            - prefix_sum[x2 + 1][y1],
            - prefix_sum[x1][y2 + 1],
            prefix_sum[x1][y1],

