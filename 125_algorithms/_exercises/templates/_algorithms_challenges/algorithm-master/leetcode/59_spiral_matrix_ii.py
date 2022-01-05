c_ Solution:
    ___ generateMatrix  n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        __ n.. n o. n < 1:
            r.. []
        __ n __ 1:
            r.. [[1]]

        ans = [[0] * n ___ _ __ r..(n)]
        delta = (
            (0, 1), (1, 0),
            (0, -1), (-1, 0),
        )
        x = y = turn = 0

        ___ i __ r..(1, n * n + 1):
            ans[x][y] = i
            _x = x + delta[turn][0]
            _y = y + delta[turn][1]

            __ n.. (0 <= _x < n a.. 0 <= _y < n) o. ans[_x][_y] != 0:
                turn = (turn + 1) % l..(delta)
                _x = x + delta[turn][0]
                _y = y + delta[turn][1]

            x = _x
            y = _y

        r.. ans
