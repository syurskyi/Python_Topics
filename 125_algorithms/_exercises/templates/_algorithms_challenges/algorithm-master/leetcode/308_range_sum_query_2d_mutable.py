"""
Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
obj.update(x,y,val)
param_1 = obj.sumRegion(x1,y1,x2,y2)
"""


class NumMatrix:
    ___ __init__(self, matrix
        """
        :type matrix: List[List[int]]
        """
        __ not matrix or not matrix[0]:
            r_

        m, n = le.(matrix), le.(matrix[0])
        self.bits = [[0] * (n + 1) for _ in range(m + 1)]  # bits
        self.incr = [[0] * (n + 1) for _ in range(m + 1)]  # increments

        for x in range(m
            for y in range(n
                self.update(x, y, matrix[x][y])

    ___ update(self, x, y, val
        """
        :type x: int
        :type y: int
        :type val: int
        :rtype: void
        """
        i = x + 1
        j = y + 1

        delta = val - self.incr[i][j]
        self.incr[i][j] = val

        m, n = le.(self.incr), le.(self.incr[0])

        w___ i < m:
            j = y + 1
            w___ j < n:
                self.bits[i][j] += delta
                j += (j & -j)
            i += (i & -i)

    ___ sumRegion(self, x1, y1, x2, y2
        """
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: int
        """
        r_ sum((
            self.sum(x2 + 1, y2 + 1),
            - self.sum(x1, y2 + 1),
            - self.sum(x2 + 1, y1),
            self.sum(x1, y1),
        ))

    ___ sum(self, x, y
        res = 0
        i = x
        j = y

        w___ i > 0:
            j = y
            w___ j > 0:
                res += self.bits[i][j]
                j -= (j & -j)
            i -= (i & -i)

        r_ res
