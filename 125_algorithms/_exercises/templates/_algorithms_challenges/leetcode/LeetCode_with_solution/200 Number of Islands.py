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


c_ Solution:
    ___ - ):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ___ numIslands(self, grid):
        """
        :type grid: list[list[str]]
        :rtype: int
        """
        m = l..(grid)
        __ m < 1:
            r.. 0
        n = l..(grid[0])
        __ n < 1:
            r.. 0

        cnt = 0
        visited = [[F.. ___ _ __ xrange(n)] ___ _ __ xrange(m)]
        ___ i __ xrange(m):
            ___ j __ xrange(n):
                __ n.. visited[i][j] a.. grid[i][j] __ "1":
                    dfs(grid, i, j, visited)
                    cnt += 1

        r.. cnt

    ___ dfs(self, grid, i, j, visited):
        """
        dfs to mark visited
        """
        m = l..(grid)
        n = l..(grid[0])
        visited[i][j] = T..

        ___ dir __ dirs:
            I = i+dir[0]
            J = j+dir[1]
            __ 0 <= I < m a.. 0 <= J < n a.. n.. visited[I][J] a.. grid[I][J] __ "1":
                dfs(grid, I, J, visited)


__ _______ __ _______
    ... Solution().numIslands(["1", "1"]) __ 1