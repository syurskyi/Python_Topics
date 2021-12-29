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

        for _ in range(K + 1):
            for u, v, cost in flights:
                costs[v] = min(costs[v], min_cost[u] + cost)
            min_cost = costs

        return costs[dst] __ costs[dst] < float('inf') else -1


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
        __ src == dst:
            return 0

        INF = float('inf')

        """
        `dp[i][k]` means the cost when the end is `i` with `k` stop
        """
        dp = [[INF] * (K + 1) for _ in range(n)]
        dp[src][0] = 0

        for start, end, cost in flights:
            __ start == src and cost < dp[end][0]:
                dp[end][0] = cost

        for k in range(1, K + 1):
            for i in range(n):
                dp[i][k] = dp[i][k - 1]

            for start, end, cost in flights:
                dp[end][k] = min(
                    dp[end][k],
                    dp[start][k - 1] + cost
                )

        return dp[dst][K] __ dp[dst][K] < INF else -1
