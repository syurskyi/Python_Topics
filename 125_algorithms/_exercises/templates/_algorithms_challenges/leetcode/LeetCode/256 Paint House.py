"""
Premium Question
"""
______ sys

__author__ = 'Daniel'


class Solution:
    # @param {integer[][]} costs
    # @return {integer}
    ___ minCost(self, costs
        """
        Lef F[i][j] be the total min costs when the houses BEFORE i are painted, with (i-1)-th house pained as color j
        :type costs: list[list[int]]
        :rtype: int
        """
        __ not costs:
            r_ 0

        n = le.(costs)
        m = le.(costs[0])
        F = [[0 ___ _ in xrange(m)] ___ _ in xrange(n+1)]
        ___ k in xrange(1, n+1
            ___ i in xrange(m
                F[k][i] = sys.maxint
                ___ j in xrange(m
                    __ i != j:
                        F[k][i] = min(F[k][i], F[k-1][j]+costs[k-1][i])

        r_ min(F[n][i] ___ i in xrange(m))


__ __name__ __ "__main__":
    costs = [[7, 6, 2]]
    assert Solution().minCost(costs) __ 2