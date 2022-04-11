"""
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
__author__ 'Danyang'
c_ Solution:
    ___ subsetsWithDup  S
        """
        dfs
        notice the skipping
        :param S: a list of integer
        :return: a list of lists of integer
        """
        S.s..()
        result    # list
        get_subset(S, [], result)
        r.. result

    ___ get_subset  S, current, result
        result.a..(current)
        ___ ind, val __ e..(S
            # JUMP, avoid duplicates
            __ ind-1>_0 a.. val__S[ind-1]:  # ensure uni-direction
                _____
            get_subset(S[ind+1:], current+[val], result)


__ _____ __ ____
    print Solution().subsetsWithDup([1, 2, 3])