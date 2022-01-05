"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it
will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
"""
__author__ = 'Daniel'


c_ Solution:
    ___ rob  nums):
        """
        DP
        O(n)
        Let F_i be max value END AT or BEFORE i
        F_i = max(F_{i-1}, F_{i-2} + A[i])

        Notes:
        If change the definition of F_i
        Let F_i be mex value END AT i
        F_i = max(F_{i-2-k}+A[i] for k \in [0, i-2]),
        Then time complexity is quadratic
        """
        n = l..(nums)
        f = [0 ___ _ __ xrange(n+2)]
        ___ i __ xrange(2, n+2):
            f[i] = m..(
                f[i-1],
                f[i-2] + nums[i-2]
            )

        r.. f[-1]





