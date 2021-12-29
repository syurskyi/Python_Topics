_______ collections


class Solution:
    """
    DP:
    1. init the first pos as 1
    2. keep simulate the process and divide the probability
    3. sum the values
    """
    ___ knightProbability(self, n, k, r, c):
        """
        :type n: int
        :type k: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = collections.defaultdict(int)
        dp[r, c] = 1.0

        ___ _ __ r..(k):
            nxt = collections.defaultdict(int)

            ___ x __ r..(n):
                ___ y __ r..(n):
                    ___ dx, dy __ (
                        (-1, -2),
                        ( 1, -2),
                        (-2, -1),
                        ( 2, -1),
                        (-2,  1),
                        ( 2,  1),
                        (-1,  2),
                        ( 1,  2),
                    ):
                        _x = x + dx
                        _y = y + dy

                        __ n.. (0 <= _x < n and 0 <= _y < n):
                            continue

                        nxt[_x, _y] += dp[x, y] / 8.0

            dp = nxt

        r.. s..(dp.values())


class Solution:
    """
    BFS: TLE
    """
    ___ knightProbability(self, n, k, r, c):
        """
        :type n: int
        :type k: int
        :type r: int
        :type c: int
        :rtype: float
        """
        __ n __ 1 and k __ 0:
            r.. 1.0

        queue, _queue = [(r, c)], []
        total = 8 ** k
        valid = 0

        while queue and k:
            k -= 1

            ___ x, y __ queue:
                ___ dx, dy __ (
                    (-1, -2),
                    ( 1, -2),
                    (-2, -1),
                    ( 2, -1),
                    (-2,  1),
                    ( 2,  1),
                    (-1,  2),
                    ( 1,  2),
                ):
                    _x = x + dx
                    _y = y + dy

                    __ n.. (0 <= _x < n and 0 <= _y < n):
                        continue

                    __ k __ 0:
                        valid += 1

                    __ k > 0:
                        _queue.a..((_x, _y))

            queue, _queue = _queue, []

        r.. valid / total
