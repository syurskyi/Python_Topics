c_ Solution:
    ___ updateMatrix  matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        __ n.. matrix o. n.. matrix[0]:
            r.. []

        m, n = l..(matrix), l..(matrix[0])
        ans = [[f__('inf')] * n ___ _ __ r..(m)]
        queue    # list

        ___ x __ r..(m):
            ___ y __ r..(n):
                __ matrix[x][y] __ 0:
                    ans[x][y] = 0
                    queue.a..((x, y))

        ___ x, y __ queue:
            ___ dx, dy __ (
                (-1, 0), (1, 0),
                (0, -1), (0, 1),
            ):
                _x = x + dx
                _y = y + dy

                __ n.. (0 <= _x < m a.. 0 <= _y < n):
                    _____
                __ ans[_x][_y] < ans[x][y] + 1:
                    _____

                ans[_x][_y] = ans[x][y] + 1
                queue.a..((_x, _y))

        r.. ans
