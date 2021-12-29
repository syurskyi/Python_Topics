"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
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
    ___ shortestPath(self, G, S, T):
        __ n.. G o. n.. S o. n.. T:
            r.. -1

        INFINITY = float('inf')
        m, n = l..(G), l..(G[0])
        min_steps = [[INFINITY] * n ___ _ __ r..(m)]

        queue = [S]
        _queue = N..
        _x = _y = steps = 0

        while queue:
            _queue    # list
            steps += 1

            ___ P __ queue:
                ___ dx, dy __ self.V:
                    _x = P.x + dx
                    _y = P.y + dy

                    __ (0 <= _x < m and 0 <= _y < n and
                        n.. G[_x][_y] and
                        steps < min_steps[_x][_y]):

                        __ _x __ T.x and _y __ T.y:
                            r.. steps

                        min_steps[_x][_y] = steps
                        _queue.a..(Point(_x, _y))

            queue = _queue

        r.. -1
