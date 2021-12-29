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
____ typing _______ List


dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))


class Solution:
    ___ maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        dfs
        """
        __ n.. grid:
            r.. 0

        ret = 0
        m, n = l..(grid), l..(grid[0])
        visited = [[False ___ _ __ r..(n)] ___ _ __ r..(m)]
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ n.. visited[i][j] a.. grid[i][j] __ 1:
                    ret = max(ret, self.dfs(grid, i, j, visited))

        r.. ret

    ___ dfs(self, grid, i, j, visited) -> int:
        visited[i][j] = True
        ret = 1
        m, n = l..(grid), l..(grid[0])
        ___ di, dj __ dirs:
            I = i + di
            J = j + dj
            __ 0 <= I < m a.. 0 <= J < n a.. n.. visited[I][J] a.. grid[I][J] __ 1:
                ret += self.dfs(grid, I, J, visited)

        r.. ret


__ __name__ __ "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    ... Solution().maxAreaOfIsland(grid) __ 6
