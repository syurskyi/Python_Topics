c_ Solution:
    """
    BFS
    """
    ___ coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = 0

        __ n.. coins o. n.. amount:
            r.. ans

        queue, _queue = [0], []
        visited = set(queue)

        w.... queue:
            ans += 1

            ___ a __ queue:
                ___ c __ coins:
                    _a = a + c

                    __ _a __ amount:
                        r.. ans

                    __ _a > amount o. _a __ visited:
                        _____

                    visited.add(_a)
                    _queue.a..(_a)

            queue, _queue = _queue, []

        r.. -1


c_ Solution:
    """
    DP: TLE
    """
    ___ coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        __ n.. coins o. n.. amount:
            r.. 0

        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0

        ___ c __ coins:
            ___ a __ r..(c, amount + 1):
                # if a < c: continue
                dp[a] = m..(dp[a], dp[a - c] + 1)

        r.. dp[amount] __ dp[amount] < INF ____ -1
