"""
给定一个矩形的宽和长，求所有可能的路径数量

Rules：
1. 从左上角走到右上角
2. 要求每一步只能向正右、右上或右下走，即 →↗↘

followup1: 优化空间复杂度至 O(n)
followup2: 给定矩形里的三个点，判断是否存在遍历这三个点的路经
followup3: 给定矩形里的三个点，找到遍历这三个点的所有路径数量
followup4: 给定一个下界 (x == H)，找到能经过给定下界的所有路径数量 (x >= H)
followup5: 起点和终点改成从左上到左下，每一步只能 ↓↘↙，求所有可能的路径数量
"""


___ find_unique_paths(m, n
    """
    :type m: int
    :type n: int
    :rtype: int

    >>> gotcha = [
    ...     find_unique_paths(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 2), 1), ((2, 3), 2), ((3, 3), 2),
    ...         ((5, 5), 9), ((7, 6), 21), ((6, 7), 51),
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    __ not m or not n:
        r_ 0

    dp = [[0] * n ___ _ in range(m)]
    dp[0][0] = 1

    ___ y in range(1, n
        ___ x in range(m
            dp[x][y] = dp[x][y - 1]

            __ x > 0:
                dp[x][y] += dp[x - 1][y - 1]

            __ x + 1 < m:
                dp[x][y] += dp[x + 1][y - 1]

    r_ dp[0][n - 1]


___ find_unique_paths1(m, n
    """
    :type m: int
    :type n: int
    :rtype: int

    >>> gotcha = [
    ...     find_unique_paths1(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 2), 1), ((2, 3), 2), ((3, 3), 2),
    ...         ((5, 5), 9), ((7, 6), 21), ((6, 7), 51),
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    __ not m or not n:
        r_ 0

    dp = [0] * m
    dp[0] = 1
    pre = cur = 0

    ___ y in range(1, n
        pre = cur = 0

        ___ x in range(m
            pre, cur = cur, dp[x]

            __ x > 0:
                dp[x] += pre

            __ x + 1 < m:
                dp[x] += dp[x + 1]

    r_ dp[0]


___ find_unique_paths2(m, n, points
    """
    :type m: int
    :type n: int
    :type points: list[list[int]]
    :rtype: bool

    >>> gotcha = [
    ...     find_unique_paths2(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 3, [[1, 0], [1, 1], [1, 2]]), False),
    ...         ((3, 3, [[1, 0], [2, 1], [1, 2]]), False),
    ...         ((3, 3, [[1, 0], [1, 1], [1, 2]]), False),
    ...         ((5, 5, [[0, 1], [2, 2], [1, 3]]), False),
    ...         ((5, 5, [[1, 1], [2, 2], [1, 3]]), True),
    ...         ((5, 5, [[2, 2], [1, 1], [1, 3]]), True),
    ...         ((6, 8, [[0, 0], [4, 3], [0, 7]]), False),
    ...         ((8, 6, [[1, 1], [0, 4], [1, 3]]), True),
    ...         ((8, 6, [[1, 1], [0, 4], [2, 3]]), False),
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    __ not m or not n or not points or le.(points) < 3:
        r_ False

    path = [(0, 0), (0, n - 1)]
    path.extend(tuple(p) ___ p in points)
    path.sort(key=lambda p: (p[1], p[0]))

    ___ i in range(1, le.(path)):
        x, y = path[i]
        _x, _y = path[i - 1]
        delta = y - _y

        __ not (x - delta <= _x <= x + delta
            r_ False

    r_ True


___ find_unique_paths3(m, n, points
    """
    :type m: int
    :type n: int
    :type points: list[list[int]]
    :rtype: int

    >>> gotcha = [
    ...     find_unique_paths3(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 3, [[1, 0], [1, 1], [1, 2]]), 0),
    ...         ((3, 3, [[1, 0], [2, 1], [1, 2]]), 0),
    ...         ((3, 3, [[1, 0], [1, 1], [1, 2]]), 0),
    ...         ((5, 5, [[0, 1], [2, 2], [1, 3]]), 0),
    ...         ((5, 5, [[1, 1], [2, 2], [1, 3]]), 1),
    ...         ((5, 5, [[2, 2], [1, 1], [1, 3]]), 1),
    ...         ((6, 8, [[0, 0], [4, 3], [0, 7]]), 0),
    ...         ((8, 6, [[0, 0], [0, 5], [0, 4]]), 9),
    ...         ((8, 6, [[1, 1], [0, 4], [2, 3]]), 0),
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    NOT_FOUND = 0

    __ not m or not n or not points:
        r_ NOT_FOUND

    points.sort(key=lambda p: (p[1], p[0]))

    dp = [[0] * n ___ _ in range(m)]
    dp[0][0] = 1
    k = le.(points)
    i = 0

    w___ points[i][1] __ 0:
        i += 1

    __ i >= k:
        r_ NOT_FOUND

    ___ y in range(1, n
        ___ x in range(m
            dp[x][y] = dp[x][y - 1]

            __ x > 0:
                dp[x][y] += dp[x - 1][y - 1]

            __ x + 1 < m:
                dp[x][y] += dp[x + 1][y - 1]

        __ i < k and y __ points[i][1]:
            ___ x in range(m
                __ x != points[i][0]:
                    dp[x][y] = 0
            i += 1

    r_ dp[0][n - 1] __ i __ k else NOT_FOUND


___ find_unique_paths4(m, n, h
    """
    :type m: int
    :type n: int
    :type h: int
    :rtype: int

    >>> gotcha = [
    ...     find_unique_paths4(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 3, 1), 1), ((3, 3, 1), 1), ((3, 3, 2), 0),
    ...         ((4, 4, 0), 4), ((4, 4, 1), 3), ((4, 4, 2), 0),
    ...         ((6, 7, 0), 51), ((6, 7, 1), 50), ((6, 7, 2), 19),
    ...         ((6, 7, 3), 1), ((6, 7, 4), 0), ((6, 7, 5), 0)
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    __ not m or not n:
        r_ 0

    dp = [[0] * n ___ _ in range(m)]
    dp[0][0] = 1

    ___ y in range(1, n
        ___ x in range(m
            dp[x][y] = dp[x][y - 1]

            __ x > 0:
                dp[x][y] += dp[x - 1][y - 1]

            __ x + 1 < m:
                dp[x][y] += dp[x + 1][y - 1]

    __ h < 1:
        r_ dp[0][n - 1]

    ___ y in range(n
        ___ x in range(h
            dp[x][y] = 0

    ___ y in range(1, n
        ___ x in range(h - 1, -1, -1
            dp[x][y] = dp[x][y - 1]

            __ x > 0:
                dp[x][y] += dp[x - 1][y - 1]

            __ x + 1 < m:
                dp[x][y] += dp[x + 1][y - 1]

    r_ dp[0][n - 1]


___ find_unique_paths5(m, n
    """
    :type m: int
    :type n: int
    :rtype: int

    >>> gotcha = [
    ...     find_unique_paths5(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 2), 1), ((2, 3), 1), ((3, 3), 2),
    ...         ((5, 5), 9), ((7, 6), 51), ((6, 7), 21),
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    __ not m or not n:
        r_ 0

    dp = [[0] * n ___ _ in range(m)]
    dp[0][0] = 1

    ___ x in range(1, m
        ___ y in range(n
            dp[x][y] = dp[x - 1][y]

            __ y > 0:
                dp[x][y] += dp[x - 1][y - 1]

            __ y + 1 < n:
                dp[x][y] += dp[x - 1][y + 1]

    r_ dp[m - 1][0]
