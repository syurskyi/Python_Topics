c_ Solution:
    """
    BFS
    """
    ___ shortestDistance  maze, start, destination
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int

        >>> s = Solution()
        >>> maze = [[0, 0, 1, 0, 0],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 0, 0, 1, 0],
        ...         [1, 1, 0, 1, 1],
        ...         [0, 0, 0, 0, 0]]

        >>> s.shortestDistance(maze, [0, 4], [4, 4])
        12

        >>> s.shortestDistance(maze, [0, 4], [3, 2])
        -1
        """
        __ n.. maze o. n.. maze[0]:
            r.. -1

        m, n l..(maze), l..(maze 0
        sx, sy start
        tx, ty destination
        queue [(sx, sy)]
        distance {(sx, sy 0}

        ___ x, y __ queue:
            ___ dx, dy __ ((-1, 0), (1, 0), (0, -1), (0, 1:
                _x x + dx
                _y y + dy
                _step 0

                w.... 0 <_ _x < m a.. 0 <_ _y < n a.. maze[_x][_y] __ 0:
                    _x += dx
                    _y += dy
                    _step += 1

                _x -_ dx
                _y -_ dy

                __ ((_x, _y) __ distance a..
                    distance[x, y] + _step >_ distance[_x, _y]
                    _____

                distance[_x, _y] distance[x, y] + _step

                __ _x __ tx a.. _y __ ty:
                    r.. distance[_x, _y]

                queue.a..((_x, _y

        r.. -1




_______ heapq


c_ Solution2:
    """
    Dijkstra
    """
    ___ shortestDistance  maze, start, destination
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int

        >>> s = Solution2()
        >>> maze = [[0, 0, 1, 0, 0],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 0, 0, 1, 0],
        ...         [1, 1, 0, 1, 1],
        ...         [0, 0, 0, 0, 0]]

        >>> s.shortestDistance(maze, [0, 4], [4, 4])
        12

        >>> s.shortestDistance(maze, [0, 4], [3, 2])
        -1
        """
        __ n.. maze o. n.. maze[0]:
            r.. -1

        m, n l..(maze), l..(maze 0
        sx, sy start
        tx, ty destination
        heap [(sx, sy)]
        distance {(sx, sy 0}

        w.... heap:
            x, y heapq.heappop(heap)

            ___ dx, dy __ ((-1, 0), (1, 0), (0, -1), (0, 1:
                _x x + dx
                _y y + dy

                w.... 0 <_ _x < m a.. 0 <_ _y < n a.. maze[_x][_y] __ 0:
                    _x += dx
                    _y += dy

                _x -_ dx
                _y -_ dy

                _step distance[x, y] + a..(_x - x) + a..(_y - y)

                __ (_x, _y) __ distance a.. _step >_ distance[_x, _y]:
                    _____

                __ _x __ tx a.. _y __ ty:
                    r.. _step

                distance[_x, _y] _step
                heapq.heappush(heap, (_x, _y

        r.. -1
