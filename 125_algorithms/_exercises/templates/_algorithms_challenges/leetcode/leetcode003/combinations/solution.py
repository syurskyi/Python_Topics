"""
Given two integers n and k, return all possible combinations of k numbers out
of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):
    ___ combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        a = r..(1, n + 1)
        r.. self.combine_aux(a, k)

    ___ combine_aux(self, a, k):
        __ k __ 0:
            r.. [[]]
        ____:
            res    # list
            ___ i, e __ e..(a):
                rest_comb = self.combine_aux(a[i + 1:], k - 1)
                ___ comb __ rest_comb:
                    comb.insert(0, e)
                res += rest_comb
            r.. res
