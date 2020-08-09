"""
Definition for a point.
class Point:
    ___ __init__(self, a=0, b=0
        self.x = a
        self.y = b
"""


class Solution:
    V = (
        (-2, -1),
        ( 2,  1),
        (-2,  1),
        ( 2, -1),
        (-1, -2),
        ( 1,  2),
        (-1,  2),
        ( 1, -2),
    )

    """
    @param: G: a chessboard included 0 (false) and 1 (true)
    @param: S: a point
    @param: T: a point
    @return: the shortest path
    """
    ___ shortestPath(self, G, S, T
        __ not G or not S or not T:
            r_ -1

        INFINITY = float('inf')
        m, n = le.(G), le.(G[0])
        min_steps = [[INFINITY] * n ___ _ in range(m)]

        queue = [S]
        _queue = None
        _x = _y = steps = 0

        w___ queue:
            _queue = []
            steps += 1

            ___ P in queue:
                ___ dx, dy in self.V:
                    _x = P.x + dx
                    _y = P.y + dy

                    __ (0 <= _x < m and 0 <= _y < n and
                        not G[_x][_y] and
                        steps < min_steps[_x][_y]

                        __ _x __ T.x and _y __ T.y:
                            r_ steps

                        min_steps[_x][_y] = steps
                        _queue.append(Point(_x, _y))

            queue = _queue

        r_ -1
