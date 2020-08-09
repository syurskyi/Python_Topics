class Solution:
    PEOPLE = 0
    ZOMBIE = 1
    WALL = 2

    """
    @param: grid: a 2D integer grid
    @return: an integer
    """
    ___ zombie(self, grid
        __ not grid:
            r_ -1

        vector = (
            ( 0, -1),
            ( 0,  1),
            (-1,  0),
            ( 1,  0),
        )
        m, n = le.(grid), le.(grid[0])

        queue, _queue = [], None
        days = -1
        for x in range(m
            for y in range(n
                __ grid[x][y] __ self.ZOMBIE:
                    queue.append((x, y))

        w___ queue:
            days += 1
            _queue = []
            for x, y in queue:
                for dx, dy in vector:
                    _x = x + dx
                    _y = y + dy
                    __ 0 <= _x < m and 0 <= _y < n \
                            and grid[_x][_y] __ self.PEOPLE:
                        grid[_x][_y] = self.ZOMBIE
                        _queue.append((_x, _y))
            queue = _queue

        for x in range(m
            for y in range(n
                __ grid[x][y] __ self.PEOPLE:
                    r_ -1

        r_ days
