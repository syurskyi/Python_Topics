"""
Premium Question
"""
_______ sys

__author__ = 'Daniel'


c_ Solution:
    # @param {integer[][]} costs
    # @return {integer}
    ___ minCost(self, costs):
        """
        Lef F[i][j] be the total min costs when the houses BEFORE i are painted, with (i-1)-th house pained as color j
        :type costs: list[list[int]]
        :rtype: int
        """
        __ n.. costs:
            r.. 0

        n = l..(costs)
        m = l..(costs[0])
        F = [[0 ___ _ __ xrange(m)] ___ _ __ xrange(n+1)]
        ___ k __ xrange(1, n+1):
            ___ i __ xrange(m):
                F[k][i] = sys.maxint
                ___ j __ xrange(m):
                    __ i != j:
                        F[k][i] = m..(F[k][i], F[k-1][j]+costs[k-1][i])

        r.. m..(F[n][i] ___ i __ xrange(m))


__ __name__ __ "__main__":
    costs = [[7, 6, 2]]
    ... Solution().minCost(costs) __ 2