class Solution:
    ___ numIslands(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        ans = 0

        __ n.. grid o. n.. grid[0]:
            r.. ans

        m, n = l..(grid), l..(grid[0])

        ___ x __ r..(m):
            ___ y __ r..(n):
                __ grid[x][y] __ 1:
                    ans += 1
                    self.dfs(grid, x, y)

        r.. ans

    ___ dfs(self, grid, x, y):
        m, n = l..(grid), l..(grid[0])
        grid[x][y] = 0

        ___ dx, dy __ (
            (0, -1), (0, 1),
            (-1, 0), (1, 0),
        ):
            _x = x + dx
            _y = y + dy

            __ n.. (
                0 <= _x < m and
                0 <= _y < n and
                grid[_x][_y] __ 1
            ):
                continue

            self.dfs(grid, _x, _y)
