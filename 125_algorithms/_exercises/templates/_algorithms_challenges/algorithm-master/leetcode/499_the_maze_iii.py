c_ Solution:
    """
    BFS
    """
    ___ findShortestWay  maze, ball, hole
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str

        >>> s = Solution()
        >>> maze = [[0, 0, 0, 0, 0],
        ...         [1, 1, 0, 0, 1],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 1, 0, 0, 1],
        ...         [0, 1, 0, 0, 0]]

        >>> s.findShortestWay(maze, [4, 3], [0, 1])
        'lul'

        >>> s.findShortestWay(maze, [4, 3], [3, 0])
        'impossible'
        """
        NOT_FOUND = 'impossible'

        __ n.. maze o. n.. maze[0]:
            r.. NOT_FOUND

        m, n = l..(maze), l..(maze[0])
        sx, sy = ball
        tx, ty = hole
        queue = [(sx, sy)]
        paths = {(sx, sy []}
        distance = {(sx, sy 0}

        ___ x, y __ queue:
            ___ dx, dy, dn __ (
                (-1, 0, 'u'), (1, 0, 'd'),
                (0, -1, 'l'), (0, 1, _,

                _x = x + dx
                _y = y + dy
                _step = 0

                w.... (
                    0 <= _x < m a.. 0 <= _y < n a..
                    maze[_x][_y] __ 0 a..
                    n.. (_x __ tx a.. _y __ ty)

                    _x += dx
                    _y += dy
                    _step += 1

                __ n.. (_x __ tx a.. _y __ ty
                    _x -= dx
                    _y -= dy
                    _step -= 1

                __ ((_x, _y) __ distance a..
                    distance[x, y] + _step > distance[_x, _y]
                    _____

                __ ((_x, _y) __ paths a..
                    paths[x, y] + [dn] > paths[_x, _y]
                    _____

                distance[_x, _y] = distance[x, y] + _step
                paths[_x, _y] = paths[x, y] + [dn]
                queue.a..((_x, _y

        r.. ''.j..(paths[tx, ty]) __ (tx, ty) __ paths ____ NOT_FOUND


_______ heapq


c_ Solution2:
    """
    Dijkstra
    """
    ___ findShortestWay  maze, ball, hole
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str

        >>> s = Solution2()
        >>> maze = [[0, 0, 0, 0, 0],
        ...         [1, 1, 0, 0, 1],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 1, 0, 0, 1],
        ...         [0, 1, 0, 0, 0]]

        >>> s.findShortestWay(maze, [4, 3], [0, 1])
        'lul'

        >>> s.findShortestWay(maze, [4, 3], [3, 0])
        'impossible'
        """
        NOT_FOUND = 'impossible'

        __ n.. maze o. n.. maze[0]:
            r.. NOT_FOUND

        m, n = l..(maze), l..(maze[0])
        sx, sy = ball
        tx, ty = hole
        heap = [(sx, sy)]
        paths = {(sx, sy []}
        distance = {(sx, sy 0}

        w.... heap:
            x, y = heapq.heappop(heap)

            ___ dx, dy, dn __ (
                (-1, 0, 'u'), (1, 0, 'd'),
                (0, -1, 'l'), (0, 1, _,

                _x = x + dx
                _y = y + dy

                w.... (
                    0 <= _x < m a.. 0 <= _y < n a..
                    maze[_x][_y] __ 0 a..
                    n.. (_x __ tx a.. _y __ ty)

                    _x += dx
                    _y += dy

                __ n.. (_x __ tx a.. _y __ ty
                    _x -= dx
                    _y -= dy

                _step = distance[x, y] + abs(_x - x) + abs(_y - y)

                __ (_x, _y) __ distance a.. _step > distance[_x, _y]:
                    _____

                __ (_x, _y) __ paths a.. paths[x, y] + [dn] > paths[_x, _y]:
                    _____

                distance[_x, _y] = _step
                paths[_x, _y] = paths[x, y] + [dn]
                heapq.heappush(heap, (_x, _y

        r.. ''.j..(paths[tx, ty]) __ (tx, ty) __ paths ____ NOT_FOUND
