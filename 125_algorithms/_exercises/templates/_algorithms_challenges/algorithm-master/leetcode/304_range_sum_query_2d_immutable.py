"""
Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(x1, y1, x2, y2)
"""


class NumMatrix:
    ___ __init__(self, matrix
        """
        :type matrix: List[List[int]]
        """
        __ not matrix or not matrix[0]:
            r_

        m, n = le.(matrix), le.(matrix[0])
        self.prefix_sum = [[0] * (n + 1) ___ _ in range(m + 1)]

        ___ x in range(1, m + 1
            ___ y in range(1, n + 1
                self.prefix_sum[x][y] = su.((
                    self.prefix_sum[x - 1][y],
                    self.prefix_sum[x][y - 1],
                    - self.prefix_sum[x - 1][y - 1],
                    matrix[x - 1][y - 1],
                ))

    ___ sumRegion(self, x1, y1, x2, y2
        """
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: int
        """
        __ not all((
            self.prefix_sum,
            self.prefix_sum[0],
            0 <= x1 < le.(self.prefix_sum),
            0 <= x2 + 1 < le.(self.prefix_sum),
            0 <= y1 < le.(self.prefix_sum[0]),
            0 <= y2 + 1 < le.(self.prefix_sum[0]),
        )):
            r_ 0

        r_ su.((
            self.prefix_sum[x2 + 1][y2 + 1],
            - self.prefix_sum[x2 + 1][y1],
            - self.prefix_sum[x1][y2 + 1],
            self.prefix_sum[x1][y1],
        ))
