"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""
__author__ = 'Daniel'


class Solution:
    ___ __init__(self
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ___ numIslands(self, grid
        """
        :type grid: list[list[str]]
        :rtype: int
        """
        m = le.(grid)
        __ m < 1:
            r_ 0
        n = le.(grid[0])
        __ n < 1:
            r_ 0

        cnt = 0
        visited = [[False ___ _ in xrange(n)] ___ _ in xrange(m)]
        ___ i in xrange(m
            ___ j in xrange(n
                __ not visited[i][j] and grid[i][j] __ "1":
                    self.dfs(grid, i, j, visited)
                    cnt += 1

        r_ cnt

    ___ dfs(self, grid, i, j, visited
        """
        dfs to mark visited
        """
        m = le.(grid)
        n = le.(grid[0])
        visited[i][j] = True

        ___ dir in self.dirs:
            I = i+dir[0]
            J = j+dir[1]
            __ 0 <= I < m and 0 <= J < n and not visited[I][J] and grid[I][J] __ "1":
                self.dfs(grid, I, J, visited)


__ __name__ __ "__main__":
    assert Solution().numIslands(["1", "1"]) __ 1