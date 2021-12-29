class Solution:
    ___ findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        min_cost = [float('inf')] * n  # the minimum cost to get to node
        costs = [float('inf')] * n
        min_cost[src] = costs[src] = 0

        ___ _ __ r..(K + 1):
            ___ u, v, cost __ flights:
                costs[v] = m..(costs[v], min_cost[u] + cost)
            min_cost = costs

        r.. costs[dst] __ costs[dst] < float('inf') ____ -1


class Solution:
    ___ findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        __ src __ dst:
            r.. 0

        INF = float('inf')

        """
        `dp[i][k]` means the cost when the end is `i` with `k` stop
        """
        dp = [[INF] * (K + 1) ___ _ __ r..(n)]
        dp[src][0] = 0

        ___ start, end, cost __ flights:
            __ start __ src and cost < dp[end][0]:
                dp[end][0] = cost

        ___ k __ r..(1, K + 1):
            ___ i __ r..(n):
                dp[i][k] = dp[i][k - 1]

            ___ start, end, cost __ flights:
                dp[end][k] = m..(
                    dp[end][k],
                    dp[start][k - 1] + cost
                )

        r.. dp[dst][K] __ dp[dst][K] < INF ____ -1
