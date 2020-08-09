class Solution:
    ___ numIslands(self, grid
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        ans = 0

        __ not grid or not grid[0]:
            r_ ans

        m, n = le.(grid), le.(grid[0])

        ___ x in range(m
            ___ y in range(n
                __ grid[x][y] __ 1:
                    ans += 1
                    self.dfs(grid, x, y)

        r_ ans

    ___ dfs(self, grid, x, y
        m, n = le.(grid), le.(grid[0])
        grid[x][y] = 0

        ___ dx, dy in (
            (0, -1), (0, 1),
            (-1, 0), (1, 0),

            _x = x + dx
            _y = y + dy

            __ not (
                0 <= _x < m and
                0 <= _y < n and
                grid[_x][_y] __ 1

                continue

            self.dfs(grid, _x, _y)
