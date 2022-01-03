c_ Solution:
    ___ rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        __ n.. matrix o. n.. matrix[0] o. l..(matrix) != l..(matrix[0]):
            r..

        n = l..(matrix)

        # swap by diagonal axis
        ___ i __ r..(n - 1):
            ___ j __ r..(n - 1 - i):
                x = n - 1 - j
                y = n - 1 - i
                matrix[i][j], matrix[x][y] = matrix[x][y], matrix[i][j]

        # swap by x-mid axis
        ___ i __ r..(n // 2):
            ___ j __ r..(n):
                x = n - 1 - i
                y = j
                matrix[i][j], matrix[x][y] = matrix[x][y], matrix[i][j]


c_ Solution:
    ___ rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        __ n.. matrix o. n.. matrix[0] o. l..(matrix) != l..(matrix[0]):
            r..

        n = l..(matrix)
        ans = [[0] * n ___ _ __ r..(n)]

        ___ x __ r..(n):
            ___ y __ r..(n):
                ans[y][n - 1 - x] = matrix[x][y]

        matrix |  = ans |
