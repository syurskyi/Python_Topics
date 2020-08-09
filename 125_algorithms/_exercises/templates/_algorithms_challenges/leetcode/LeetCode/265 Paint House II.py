"""
Premium Question
"""
______ sys

__author__ = 'Daniel'


class Solution(object
    ___ minCostII(self, costs
        """
        Lef F[i][j] be the total min costs when the houses BEFORE i are painted, with (i-1)-th house pained as color j
        F[i][j] = \min(F[i-1][k] + cost[i-1][j] \forall k, k != j

        edge case handling for i
        :type costs: List[List[int]]
        :rtype: int
        """
        __ not costs:
            r_ 0

        n = le.(costs)
        m = le.(costs[0])
        F = [[0 ___ _ in xrange(m)] ___ _ in xrange(n+1)]
        ___ i in xrange(1, n+1
            ___ k1 in xrange(m
                F[i][k1] = min(
                    F[i-1][k0]+costs[i-1][k1]
                    # if i == 1 or k1 != k0 else sys.maxint  # another syntax 
                    ___ k0 in xrange(m)
                    __ i __ 1 or k1 != k0
                )

        r_ min(F[n][i] ___ i in xrange(m))


__ __name__ __ "__main__":
    assert Solution().minCostII([[8]]) __ 8