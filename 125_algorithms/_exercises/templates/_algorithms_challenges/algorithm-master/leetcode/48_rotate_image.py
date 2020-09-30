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
        ___ i __ range(n - 1
            ___ j __ range(n - 1 - i
                x = n - 1 - j
                y = n - 1 - i
                matrix[i][j], matrix[x][y] = matrix[x][y], matrix[i][j]

        # swap by x-mid axis
        ___ i __ range(n // 2
            ___ j __ range(n
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
        ans = [[0] * n ___ _ __ range(n)]

        ___ x __ range(n
            ___ y __ range(n
                ans[y][n - 1 - x] = matrix[x][y]

        matrix[:] = ans[:]
