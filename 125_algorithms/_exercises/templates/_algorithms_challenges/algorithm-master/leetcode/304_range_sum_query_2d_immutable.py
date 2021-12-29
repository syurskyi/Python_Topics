"""
Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(x1, y1, x2, y2)
"""


class NumMatrix:
    ___ __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        __ n.. matrix o. n.. matrix[0]:
            r..

        m, n = l..(matrix), l..(matrix[0])
        self.prefix_sum = [[0] * (n + 1) ___ _ __ r..(m + 1)]

        ___ x __ r..(1, m + 1):
            ___ y __ r..(1, n + 1):
                self.prefix_sum[x][y] = s..((
                    self.prefix_sum[x - 1][y],
                    self.prefix_sum[x][y - 1],
                    - self.prefix_sum[x - 1][y - 1],
                    matrix[x - 1][y - 1],
                ))

    ___ sumRegion(self, x1, y1, x2, y2):
        """
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: int
        """
        __ n.. a..((
            self.prefix_sum,
            self.prefix_sum[0],
            0 <= x1 < l..(self.prefix_sum),
            0 <= x2 + 1 < l..(self.prefix_sum),
            0 <= y1 < l..(self.prefix_sum[0]),
            0 <= y2 + 1 < l..(self.prefix_sum[0]),
        )):
            r.. 0

        r.. s..((
            self.prefix_sum[x2 + 1][y2 + 1],
            - self.prefix_sum[x2 + 1][y1],
            - self.prefix_sum[x1][y2 + 1],
            self.prefix_sum[x1][y1],
        ))
