"""
DFS
"""
c_ Solution:
    """
    @param: G: a chessboard included 0 and 1
    @return: the shortest path
    """
    ___ shortestPath2  G
        NOT_FOUND = -1
        __ n.. G o. n.. G[0] o. G[0][0] __ 1:
            r.. NOT_FOUND

        V = (
            (-1,  2),
            ( 1,  2),
            (-2,  1),
            ( 2,  1),
        )
        m, n = l..(G), l..(G[0])

        queue = [(0, 0)]
        turns = {(0, 0 0}
        ___ x, y __ queue:
            ___ dx, dy __ V:
                _x = x + dx
                _y = y + dy
                __ 0 <= _x < m a.. 0 <= _y < n a.. G[_x][_y] __ 0:
                    __ (_x, _y) __ turns:
                        _____

                    turns[_x, _y] = turns[x, y] + 1

                    __ _x __ m - 1 a.. _y __ n - 1:
                        r.. turns[_x, _y]

                    queue.a..((_x, _y

        r.. NOT_FOUND


"""
DP
"""
c_ Solution:
    """
    @param: G: a chessboard included 0 and 1
    @return: the shortest path
    """
    ___ shortestPath2  G
        __ n.. G o. n.. G[0] o. G[0][0] __ 1:
            r.. -1

        INFINITY = f__('inf')

        m, n = l..(G), l..(G[0])
        dp = [[INFINITY] * 3 ___ _ __ r..(m)]
        pre2 = pre1 = curr = 0
        dp[0][curr] = 0

        """
        x and y is changed since its need from left to right
        """
        ___ y __ r..(1, n
            pre2, pre1 = pre1, curr
            curr = y % 3
            ___ x __ r..(m
                dp[x][curr] = INFINITY

                __ G[x][y] __ 1:
                    _____

                __ (x >= 2 a.. y >= 1 a.. dp[x - 2][pre1] < INFINITY a..
                    dp[x - 2][pre1] + 1 < dp[x][curr]
                    dp[x][curr] = dp[x - 2][pre1] + 1

                __ (x >= 1 a.. y >= 2 a.. dp[x - 1][pre2] < INFINITY a..
                    dp[x - 1][pre2] + 1 < dp[x][curr]
                    dp[x][curr] = dp[x - 1][pre2] + 1

                __ (x + 1 < m a.. y >= 2 a.. dp[x + 1][pre2] < INFINITY a..
                    dp[x + 1][pre2] + 1 < dp[x][curr]
                    dp[x][curr] = dp[x + 1][pre2] + 1

                __ (x + 2 < m a.. y >= 1 a.. dp[x + 2][pre1] < INFINITY a..
                    dp[x + 2][pre1] + 1 < dp[x][curr]
                    dp[x][curr] = dp[x + 2][pre1] + 1

        r.. dp[m - 1][curr] __ dp[m - 1][curr] < INFINITY ____ -1
