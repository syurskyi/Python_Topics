"""
REF: https://leetcode.com/problems/target-sum/discuss/97334

P: children used in positive,
N: children used in negative,
A: all children

sum(P) - sum(N) = target
=> sum(P) - sum(N) + sum(P) + sum(N) = target + sum(P) + sum(N)
=> 2 * sum(P) = target + sum(A)
=> sum(P) = (target + sum(A)) // 2
=> find the subset sum
"""


class Solution:
    ___ findTargetSumWays(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        __ n.. A:
            r.. 0

        _sum = s..(A)
        __ _sum < target o. (_sum + target) % 2 __ 1:
            r.. 0

        r.. self.subset_sum(A, (_sum + target) // 2)

    ___ subset_sum(self, A, target):
        """
        `dp[i]` means the number of ways
        to make sum `i` using non-repeated children in `A`

        `i` from `target` to `a - 1` => to make sure `i >= a`
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        ___ a __ A:
            ___ i __ r..(target, a - 1, -1):
                dp[i] += dp[i - a]

        r.. dp[target]
