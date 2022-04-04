c_ Solution:
    ___ spiralOrder  matrix
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans    # list

        __ n.. matrix o. n.. matrix[0]:
            r.. ans

        # need keep its order to go right, bottom, left, top
        delta = (
            (0, 1), (1, 0),
            (0, -1), (-1, 0),
        )
        m, n = l..(matrix), l..(matrix[0])
        x = y = turn = 0

        ___ _ __ r..(m * n
            ans.a..(matrix[x][y])
            matrix[x][y] = N..
            _x = x + delta[turn][0]
            _y = y + delta[turn][1]

            __ n.. (0 <_ _x < m a.. 0 <_ _y < n) o. matrix[_x][_y] __ N..
                turn = (turn + 1) % l..(delta)
                _x = x + delta[turn][0]
                _y = y + delta[turn][1]

            x = _x
            y = _y

        r.. ans
