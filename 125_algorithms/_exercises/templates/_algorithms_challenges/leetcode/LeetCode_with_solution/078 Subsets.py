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
__author__ 'Danyang'
c_ Solution:
    ___ subsets  S
        """
        Similar to permutation and combinations
        :param S: a list of integer
        :return: a list of lists of integer
        """
        S.s..()
        result    # list
        generate_subsets(S,    # list, result)
        r.. result

    ___ generate_subsets  S, current, result
        result.a..(current)
        ___ ind, val __ e..(S
            generate_subsets(S[ind+1:], current+[val], result)

__ _____ __ ____
    print Solution().subsets([1, 2, 3])