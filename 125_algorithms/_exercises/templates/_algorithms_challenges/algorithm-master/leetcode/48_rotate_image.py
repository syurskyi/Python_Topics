class Solution:
    ___ rotate(self, matrix
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        __ not matrix or not matrix[0] or le.(matrix) != le.(matrix[0]
            r_

        n = le.(matrix)

        # swap by diagonal axis
        ___ i in range(n - 1
            ___ j in range(n - 1 - i
                x = n - 1 - j
                y = n - 1 - i
                matrix[i][j], matrix[x][y] = matrix[x][y], matrix[i][j]

        # swap by x-mid axis
        ___ i in range(n // 2
            ___ j in range(n
                x = n - 1 - i
                y = j
                matrix[i][j], matrix[x][y] = matrix[x][y], matrix[i][j]


class Solution:
    ___ rotate(self, matrix
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        __ not matrix or not matrix[0] or le.(matrix) != le.(matrix[0]
            r_

        n = le.(matrix)
        ans = [[0] * n ___ _ in range(n)]

        ___ x in range(n
            ___ y in range(n
                ans[y][n - 1 - x] = matrix[x][y]

        matrix[:] = ans[:]
