"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

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
__author__ = 'Danyang'
c_ Solution:
    ___ combine  n, k):
        """
        Similar to 045 Permutation

        :param n: int
        :param k: int
        :return: a list of lists of integers
        """
        result    # list
        nums = [i+1 ___ i __ xrange(n)]  # sorted, avoid duplicate
        get_combination(k, nums, [], result)
        r.. result

    ___ get_combination  k, nums, current, result):
        __ l..(current)__k:
            result.a..(current)
            r..  # prune
        ____ l..(current)+l..(nums)<k:
            r..  # prune

        ___ ind, val __ e..(nums):
            # try:
            get_combination(k, nums[ind+1:], current+[val], result)  # list(current).append(val) is side-effect
            # except IndexError:
            #     self.get_combination(k, [], current+[val], result)
            # array slice out of index will return []


__ _____ __ ____
    print Solution().combine(4, 2)