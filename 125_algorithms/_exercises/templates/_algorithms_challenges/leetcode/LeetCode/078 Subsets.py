"""
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
__author__ = 'Danyang'
class Solution:
    ___ subsets(self, S
        """
        Similar to permutation and combinations
        :param S: a list of integer
        :return: a list of lists of integer
        """
        S.sort()
        result =   # list
        self.generate_subsets(S,   # list, result)
        r_ result

    ___ generate_subsets(self, S, current, result
        result.append(current)
        ___ ind, val __ enumerate(S
            self.generate_subsets(S[ind+1:], current+[val], result)

__ __name____"__main__":
    print Solution().subsets([1, 2, 3])