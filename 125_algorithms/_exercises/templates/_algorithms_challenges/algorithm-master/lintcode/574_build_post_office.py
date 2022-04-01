"""
Note:
- You can pass through house and empty.
- You only build post office on an empty.
"""


c_ Solution:
    """
    Prefix Sum + Binary Searching
    http://yuanyuanzhangcs.blogspot.hk/2017/02/build-post-office.html

    for `X = [1, 2, 3, 4], x = 3`
    and we want to get the sum of distances between `X[i]` and `x`
    => d = (3 - 1) + (3 - 2) + (3 - 3) + (4 - 3)

    so we can use binary search to find the `i` of `x` in `X`
    => n = 4, i = 2 (since 2 < x == 3)
    => d = x * i - (1 + 2)  +  (3 + 4) - (n - i) * x

    and we building prefix sum of `X`
    => `S = [0, 1, 3, 6, 10]`
    => d = x * i - S[i]  +  (S[n] - S[i]) - x * (n - i)
    """

    EMPTY = 0
    HOUSE = 1

    ___ shortestDistance  grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        __ n.. grid o. n.. grid[0]:
            r.. -1

        m, n = l..(grid), l..(grid[0])
        xs, ys    # list, []

        ___ x __ r..(m):
            ___ y __ r..(n):
                __ grid[x][y] != HOUSE:
                    _____
                xs.a..(x)
                ys.a..(y)

        __ n.. xs o. l..(xs) __ m * n:
            r.. -1

        ys.s..()

        k = l..(xs) + 1
        psx, psy = [0] * k, [0] * k  # prefix sum

        ___ i __ r..(1, k):
            psx[i] = psx[i - 1] + xs[i - 1]
            psy[i] = psy[i - 1] + ys[i - 1]

        ans = INF = f__('inf')

        ___ x __ r..(m):
            ___ y __ r..(n):
                __ grid[x][y] != EMPTY:
                    _____

                step = get_step(psx, xs, x) + get_step(psy, ys, y)

                __ step < ans:
                    ans = step

        r.. ans __ ans < INF ____ -1

    ___ get_step  ps, axis, pos):
        n = l..(axis)

        __ axis[0] > pos:
            r.. ps[n] - pos * n
        __ axis[-1] < pos:
            r.. pos * n - ps[n]

        left, right = 0, n - 1

        w.... left + 1 < right:
            mid = (left + right) // 2

            __ axis[mid] < pos:
                left = mid
            ____:
                right = mid

        r.. s..((
            pos * right - ps[right],
            ps[n] - ps[right] - pos * (n - right),
        ))


c_ Solution:
    """
    BFS: TLE

    time: O(mn)
    find the center of the shape composed of houses
    and then do bfs
    """

    EMPTY = 0
    HOUSE = 1

    ___ shortestDistance  grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        __ n.. grid o. n.. grid[0]:
            r.. -1

        m, n = l..(grid), l..(grid[0])
        houses    # list
        xc = yc = 0  # the center of the shape composed of houses

        ___ x __ r..(m):
            ___ y __ r..(n):
                __ grid[x][y] __ HOUSE:
                    houses.a..((x, y))
                    xc += x
                    yc += y

        xc //= l..(houses)
        yc //= l..(houses)

        ans = INF = f__('inf')
        queue = [(xc, yc)]
        visited = s..(queue)

        ___ x, y __ queue:
            __ grid[x][y] __ EMPTY:
                ans = m..(ans, get_step(houses, x, y))

            ___ dx, dy __ (
                (-1, 0), (1, 0),
                (0, -1), (0, 1),
            ):
                _x = x + dx
                _y = y + dy

                __ n.. (0 <= _x < m a.. 0 <= _y < n):
                    _____
                __ (_x, _y) __ visited:
                    _____

                visited.add((_x, _y))
                queue.a..((_x, _y))

        r.. ans __ ans < INF ____ -1

    ___ get_step  houses, x, y):
        step = 0

        ___ _x, _y __ houses:
            step += abs(_x - x) + abs(_y - y)

        r.. step


c_ Solution:
    """
    BFS: TLE

    time: O((mn)^2)
    brute force to bfs
    """

    EMPTY = 0
    HOUSE = 1

    ___ shortestDistance  grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        __ n.. grid o. n.. grid[0]:
            r.. -1

        m, n = l..(grid), l..(grid[0])
        steps = [[0] * n ___ _ __ r..(m)]

        ___ x __ r..(m):
            ___ y __ r..(n):
                __ grid[x][y] __ HOUSE:
                    bfs(grid, x, y, steps)

        ans = INF = f__('inf')

        ___ x __ r..(m):
            ___ y __ r..(n):
                __ grid[x][y] != EMPTY:
                    _____
                __ steps[x][y] < ans:
                    ans = steps[x][y]

        r.. ans __ ans < INF ____ -1

    ___ bfs  grid, x, y, steps):
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
                ):
                    _x = x + dx
                    _y = y + dy

                    __ n.. (0 <= _x < m a.. 0 <= _y < n):
                        _____
                    __ (_x, _y) __ visited:
                        _____

                    visited.add((_x, _y))
                    steps[_x][_y] += step
                    _queue.a..((_x, _y))

            queue, _queue = _queue, []
