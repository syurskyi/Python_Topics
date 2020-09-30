"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""
__author__ = 'Danyang'
class Solution:
    ___ combinationSum(self, candidates, target
        """
        dfs

        Notice that possible to repeat
        :param candidates: a lis of integers
        :param target: target, integer
        :return: a list of lists of integers
        """
        candidates.sort()
        result =   # list
        self.get_combination(target, candidates,   # list, result)
        r_ result

    ___ get_combination(self, target, candidates, current, result
        __ not candidates or su.(current)>target:
            r_
        __ su.(current)__target:
            result.append(current)
            r_

        # add one of from the candidates
        ___ ind, val __ enumerate(candidates
            self.get_combination(target, candidates[ind:], current+[val], result)  # candidates[ind:] since possible repeat



__ __name____"__main__":
    print Solution().combinationSum([2,3,6,7], 7)