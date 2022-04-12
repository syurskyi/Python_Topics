c_ Solution:
    """
    @param: costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    ___ minCost  costs
        __ n.. costs:
            r.. 0

        INFINITY f__('inf')
        m, n l..(costs), l..(costs 0
        dp [[0] * n ___ _ __ r..(2)]

        """
        i: `i`th house
        j: `j`th color
        k: the used `k`th color in previous house
        """
        i j k prev curr 0
        ___ j __ r..(n
            dp[0][j] costs[0][j]
        ___ i __ r..(1, m
            prev curr # (i - 1) % 2
            curr i % 2
            ___ j __ r..(n
                dp[curr][j] INFINITY
                ___ k __ r..(n
                    __ k !_ j a.. dp[prev][k] + costs[i][j] < dp[curr][j]:
                        dp[curr][j] dp[prev][k] + costs[i][j]

        """
        curr == (m - 1) % 2
        """
        r.. m..(dp[curr])
