c_ Solution:
    """
    @param matrix : the martix
    @return: the distance of grid to the police
    """
    ___ policeDistance  matrix):
        m, n = l..(matrix), l..(matrix)

        POLICE = 1
        WALL = -1
        EMPTY = 0

        ans = [[f__('inf')] * n ___ _ __ r..(m)]
        queue    # list

        ___ x __ r..(m):
            ___ y __ r..(n):
                __ matrix[x][y] __ WALL:
                    ans[x][y] = -1
                ____ matrix[x][y] __ POLICE:
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
                __ matrix[_x][_y] __ WALL:
                    _____
                __ ans[_x][_y] <= ans[x][y] + 1:
                    _____

                ans[_x][_y] = ans[x][y] + 1
                queue.a..((_x, _y))

        r.. ans
