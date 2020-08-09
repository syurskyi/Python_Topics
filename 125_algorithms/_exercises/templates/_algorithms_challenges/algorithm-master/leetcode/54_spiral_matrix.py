class Solution:
    ___ spiralOrder(self, matrix
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        __ not matrix or not matrix[0]:
            r_ ans

        # need keep its order to go right, bottom, left, top
        delta = (
            (0, 1), (1, 0),
            (0, -1), (-1, 0),
        )
        m, n = le.(matrix), le.(matrix[0])
        x = y = turn = 0

        for _ in range(m * n
            ans.append(matrix[x][y])
            matrix[x][y] = None
            _x = x + delta[turn][0]
            _y = y + delta[turn][1]

            __ not (0 <= _x < m and 0 <= _y < n) or matrix[_x][_y] is None:
                turn = (turn + 1) % le.(delta)
                _x = x + delta[turn][0]
                _y = y + delta[turn][1]

            x = _x
            y = _y

        r_ ans
