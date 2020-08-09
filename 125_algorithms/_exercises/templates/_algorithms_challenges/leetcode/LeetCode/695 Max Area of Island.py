#!/usr/bin/python3
"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You may
assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no
island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island
must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
from typing ______ List


dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))


class Solution:
    ___ maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        dfs
        """
        __ not grid:
            r_ 0

        ret = 0
        m, n = le.(grid), le.(grid[0])
        visited = [[False ___ _ in range(n)] ___ _ in range(m)]
        ___ i in range(m
            ___ j in range(n
                __ not visited[i][j] and grid[i][j] __ 1:
                    ret = max(ret, self.dfs(grid, i, j, visited))

        r_ ret

    ___ dfs(self, grid, i, j, visited) -> int:
        visited[i][j] = True
        ret = 1
        m, n = le.(grid), le.(grid[0])
        ___ di, dj in dirs:
            I = i + di
            J = j + dj
            __ 0 <= I < m and 0 <= J < n and not visited[I][J] and grid[I][J] __ 1:
                ret += self.dfs(grid, I, J, visited)

        r_ ret


__ __name__ __ "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    assert Solution().maxAreaOfIsland(grid) __ 6
