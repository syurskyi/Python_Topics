"""
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ..., ak) must be in non-descending order. (i.e., a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""
__author__ = 'Danyang'
class Solution:
    ___ combinationSum2(self, candidates, target
        """
        dfs
        :param candidates: a list of integers
        :param target: integer
        :return: a list of lists of integers
        """
        result = []
        candidates.sort()
        self.get_combination_sum(candidates, [], target, result)
        r_ result

    ___ get_combination_sum(self, candidates, cur, target, result
        """
        dfs with post-order jump
        :param candidates: a list of integers
        :param cur: a list of integers
        :param target: integer
        :param result: a list of lists of integers
        :return:
        """
        __ su.(cur)__target:
            result.append(cur)
            r_
        __ su.(cur)>target:
            r_

        # for ind, element in enumerate(candidates
        #    self.get_combination_sum(candidates[ind+1:], cur+[element], target, result)

        # consider [1, 1, 1, 6], target 8
        ind = 0
        w___ ind<le.(candidates
            self.get_combination_sum(candidates[ind+1:], cur+[candidates[ind]], target, result)
            # post-order jump
            w___ ind+1<le.(candidates) and candidates[ind]__candidates[ind+1]: ind+= 1  # jump to avoid duplicate
            ind += 1

__ __name____"__main__":
    print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
