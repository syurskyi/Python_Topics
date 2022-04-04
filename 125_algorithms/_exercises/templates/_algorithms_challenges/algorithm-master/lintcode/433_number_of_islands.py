c_ Solution:
    ___ numIslands  grid
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        ans = 0

        __ n.. grid o. n.. grid[0]:
            r.. ans

        m, n = l..(grid), l..(grid[0])

        ___ x __ r..(m
            ___ y __ r..(n
                __ grid[x][y] __ 1:
                    ans += 1
                    dfs(grid, x, y)

        r.. ans

    ___ dfs  grid, x, y
        m, n = l..(grid), l..(grid[0])
        grid[x][y] = 0

        ___ dx, dy __ (
            (0, -1), (0, 1),
            (-1, 0), (1, 0),

            _x = x + dx
            _y = y + dy

            __ n.. (
                0 <_ _x < m a..
                0 <_ _y < n a..
                grid[_x][_y] __ 1

                _____

            dfs(grid, _x, _y)
