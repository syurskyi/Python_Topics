"""
DFS
"""
class Solution:
    """
    @param: G: a chessboard included 0 and 1
    @return: the shortest path
    """
    ___ shortestPath2(self, G
        NOT_FOUND = -1
        __ not G or not G[0] or G[0][0] __ 1:
            r_ NOT_FOUND

        V = (
            (-1,  2),
            ( 1,  2),
            (-2,  1),
            ( 2,  1),
        )
        m, n = le.(G), le.(G[0])

        queue = [(0, 0)]
        turns = {(0, 0 0}
        ___ x, y __ queue:
            ___ dx, dy __ V:
                _x = x + dx
                _y = y + dy
                __ 0 <= _x < m and 0 <= _y < n and G[_x][_y] __ 0:
                    __ (_x, _y) __ turns:
                        continue

                    turns[_x, _y] = turns[x, y] + 1

                    __ _x __ m - 1 and _y __ n - 1:
                        r_ turns[_x, _y]

                    queue.append((_x, _y))

        r_ NOT_FOUND


"""
DP
"""
class Solution:
    """
    @param: G: a chessboard included 0 and 1
    @return: the shortest path
    """
    ___ shortestPath2(self, G
        __ not G or not G[0] or G[0][0] __ 1:
            r_ -1

        INFINITY = float('inf')

        m, n = le.(G), le.(G[0])
        dp = [[INFINITY] * 3 ___ _ __ range(m)]
        pre2 = pre1 = curr = 0
        dp[0][curr] = 0

        """
        x and y is changed since its need from left to right
        """
        ___ y __ range(1, n
            pre2, pre1 = pre1, curr
            curr = y % 3
            ___ x __ range(m
                dp[x][curr] = INFINITY

                __ G[x][y] __ 1:
                    continue

                __ (x >= 2 and y >= 1 and dp[x - 2][pre1] < INFINITY and
                    dp[x - 2][pre1] + 1 < dp[x][curr]
                    dp[x][curr] = dp[x - 2][pre1] + 1

                __ (x >= 1 and y >= 2 and dp[x - 1][pre2] < INFINITY and
                    dp[x - 1][pre2] + 1 < dp[x][curr]
                    dp[x][curr] = dp[x - 1][pre2] + 1

                __ (x + 1 < m and y >= 2 and dp[x + 1][pre2] < INFINITY and
                    dp[x + 1][pre2] + 1 < dp[x][curr]
                    dp[x][curr] = dp[x + 1][pre2] + 1

                __ (x + 2 < m and y >= 1 and dp[x + 2][pre1] < INFINITY and
                    dp[x + 2][pre1] + 1 < dp[x][curr]
                    dp[x][curr] = dp[x + 2][pre1] + 1

        r_ dp[m - 1][curr] __ dp[m - 1][curr] < INFINITY else -1
