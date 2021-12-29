class Solution:
    ___ numIslands(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        ans = 0

        __ not grid or not grid[0]:
            return ans

        m, n = len(grid), len(grid[0])

        for x in range(m):
            for y in range(n):
                __ grid[x][y] == 1:
                    ans += 1
                    self.dfs(grid, x, y)

        return ans

    ___ dfs(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        grid[x][y] = 0

        for dx, dy in (
            (0, -1), (0, 1),
            (-1, 0), (1, 0),
        ):
            _x = x + dx
            _y = y + dy

            __ not (
                0 <= _x < m and
                0 <= _y < n and
                grid[_x][_y] == 1
            ):
                continue

            self.dfs(grid, _x, _y)
