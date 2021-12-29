class Solution:
    ___ hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool

        >>> s = Solution()
        >>> maze = [[0, 0, 1, 0, 0],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 0, 0, 1, 0],
        ...         [1, 1, 0, 1, 1],
        ...         [0, 0, 0, 0, 0]]

        >>> s.hasPath(maze, [0, 4], [4, 4])
        True

        >>> s.hasPath(maze, [0, 4], [3, 2])
        False
        """
        __ n.. maze o. n.. maze[0] o. n.. start o. n.. destination:
            r.. False

        x, y = start
        tx, ty = destination
        visited = set()
        r.. self.dfs(maze, x, y, tx, ty, visited)

    ___ dfs(self, maze, x, y, tx, ty, visited):
        __ x __ tx a.. y __ ty:
            r.. True
        __ (x, y) __ visited:
            r.. False

        visited.add((x, y))

        m, n = l..(maze), l..(maze[0])

        ___ dx, dy __ ((-1, 0), (1, 0), (0, -1), (0, 1)):
            _x = x + dx
            _y = y + dy

            w.... 0 <= _x < m a.. 0 <= _y < n a.. maze[_x][_y] __ 0:
                _x += dx
                _y += dy

            # since for now its means the position of wall
            _x -= dx
            _y -= dy

            __ self.dfs(maze, _x, _y, tx, ty, visited):
                r.. True

        r.. False
