"""
Premium Question
"""
_______ ___

__author__ 'Daniel'


c_ Solution(o..
    ___ minCostII  costs
        """
        Lef F[i][j] be the total min costs when the houses BEFORE i are painted, with (i-1)-th house pained as color j
        F[i][j] = \min(F[i-1][k] + cost[i-1][j] \forall k, k != j

        edge case handling for i
        :type costs: List[List[int]]
        :rtype: int
        """
        __ n.. costs:
            r.. 0

        n l..(costs)
        m l..(costs[0])
        F [[0 ___ _ __ x..(m)] ___ _ __ x..(n+1)]
        ___ i __ x..(1, n+1
            ___ k1 __ x..(m
                F[i][k1] m..(
                    F[i-1][k0]+costs[i-1][k1]
                    # if i == 1 or k1 != k0 else sys.maxint  # another syntax 
                    ___ k0 __ x..(m)
                    __ i __ 1 o. k1 != k0
                )

        r.. m..(F[n][i] ___ i __ x..(m


__ _______ __ _______
    ... Solution().minCostII([[8]]) __ 8