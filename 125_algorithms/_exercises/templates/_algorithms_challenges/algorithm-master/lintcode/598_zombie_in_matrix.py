c_ Solution:
    PEOPLE = 0
    ZOMBIE = 1
    WALL = 2

    """
    @param: grid: a 2D integer grid
    @return: an integer
    """
    ___ zombie  grid):
        __ n.. grid:
            r.. -1

        vector = (
            ( 0, -1),
            ( 0,  1),
            (-1,  0),
            ( 1,  0),
        )
        m, n = l..(grid), l..(grid[0])

        queue, _queue    # list, N..
        days = -1
        ___ x __ r..(m):
            ___ y __ r..(n):
                __ grid[x][y] __ ZOMBIE:
                    queue.a..((x, y))

        w.... queue:
            days += 1
            _queue    # list
            ___ x, y __ queue:
                ___ dx, dy __ vector:
                    _x = x + dx
                    _y = y + dy
                    __ 0 <= _x < m a.. 0 <= _y < n \
                            a.. grid[_x][_y] __ PEOPLE:
                        grid[_x][_y] = ZOMBIE
                        _queue.a..((_x, _y))
            queue = _queue

        ___ x __ r..(m):
            ___ y __ r..(n):
                __ grid[x][y] __ PEOPLE:
                    r.. -1

        r.. days
