"""
Note:
- You cannot pass through wall and house, but can pass through empty.
- You only build post office on an empty.
"""


_______ c..


c_ Solution:
    """
    BFS

    1. for each house, use `BFS` in level traversal
       to count the distance if the cell is empty and reachable
    2. find the minimum of the total distance in each empty cell,
       and it must be reachable for each house
    """

    EMPTY = 0
    HOUSE = 1
    WALL = 2

    ___ shortestDistance  grid
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        __ n.. grid o. n.. grid[0]:
            r.. -1

        m, n = l..(grid), l..(grid[0])
        cnt = 0
        times = c...d..(i..)
        steps = c...d..(i..)

        ___ x __ r..(m
            ___ y __ r..(n
                __ grid[x][y] __ HOUSE:
                    cnt += 1
                    bfs(grid, x, y, times, steps)

        ans = INF = f__('inf')

        ___ (x, y), t __ times.i..:
            __ t __ cnt a.. steps[x, y] < ans:
                ans = steps[x, y]

        r.. ans __ ans < INF ____ -1

    ___ bfs  grid, x, y, times, steps
        m, n = l..(grid), l..(grid[0])
        queue, _queue = [(x, y)], []
        visited = s..(queue)
        step = 0

        w.... queue:
            step += 1

            ___ x, y __ queue:
                ___ dx, dy __ (
                    (-1, 0), (1, 0),
                    (0, -1), (0, 1),

                    _x = x + dx
                    _y = y + dy

                    __ n.. (0 <_ _x < m a.. 0 <_ _y < n
                        _____
                    __ grid[_x][_y] != EMPTY:
                        _____
                    __ (_x, _y) __ visited:
                        _____

                    visited.add((_x, _y
                    _queue.a..((_x, _y

                    steps[_x, _y] += step
                    times[_x, _y] += 1

            queue, _queue = _queue, []


_______ c..


c_ Solution:
    """
    DFS: TLE

    If use DFS, need to consider update min dist
    so may visit a node many times
    """

    EMPTY = 0
    HOUSE = 1
    WALL = 2

    ___ shortestDistance  grid
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        __ n.. grid o. n.. grid[0]:
            r.. -1

        m, n = l..(grid), l..(grid[0])
        cnt = 0
        ids = c...d..(s..)  # record house ids
        steps = c...d..(i..)  # total steps for all houses

        ___ x __ r..(m
            ___ y __ r..(n
                __ grid[x][y] != HOUSE:
                    _____

                cnt += 1
                step = c...d..(i..)  # steps for current house
                dfs(grid, x, y, cnt, ids, steps, step)

        ans = INF = f__('inf')

        ___ (x, y), hids __ ids.i..:
            __ l..(hids) __ cnt a.. steps[x, y] < ans:
                ans = steps[x, y]

        r.. ans __ ans < INF ____ -1

    ___ dfs  grid, x, y, id, ids, steps, step
        m, n = l..(grid), l..(grid[0])

        ___ dx, dy __ (
            (-1, 0), (1, 0),
            (0, -1), (0, 1),

            _x = x + dx
            _y = y + dy

            __ n.. (0 <_ _x < m a.. 0 <_ _y < n
                _____
            __ grid[_x][_y] != EMPTY:
                _____
            __ step[x, y] + 1 >_ step[_x, _y] > 0:  # > 0 means visited, since its defaultdict
                _____

            ids[_x, _y].add(id)

            steps[_x, _y] -= step[_x, _y]
            step[_x, _y] = step[x, y] + 1
            steps[_x, _y] += step[_x, _y]

            dfs(grid, _x, _y, id, ids, steps, step)
