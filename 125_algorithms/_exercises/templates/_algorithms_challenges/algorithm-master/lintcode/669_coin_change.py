class Solution:
    """
    BFS
    """
    ___ coinChange(self, coins, amount
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = 0

        __ not coins or not amount:
            r_ ans

        queue, _queue = [0], []
        visited = set(queue)

        w___ queue:
            ans += 1

            ___ a in queue:
                ___ c in coins:
                    _a = a + c

                    __ _a __ amount:
                        r_ ans

                    __ _a > amount or _a in visited:
                        continue

                    visited.add(_a)
                    _queue.append(_a)

            queue, _queue = _queue, []

        r_ -1


class Solution:
    """
    DP: TLE
    """
    ___ coinChange(self, coins, amount
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        __ not coins or not amount:
            r_ 0

        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0

        ___ c in coins:
            ___ a in range(c, amount + 1
                # if a < c: continue
                dp[a] = min(dp[a], dp[a - c] + 1)

        r_ dp[amount] __ dp[amount] < INF else -1
