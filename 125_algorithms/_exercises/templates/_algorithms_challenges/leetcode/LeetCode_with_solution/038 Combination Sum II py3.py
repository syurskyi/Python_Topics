#!/usr/bin/python3
"""
Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate numbers
sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
____ typing _______ List


class Solution:
    ___ combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret    # list
        candidates.sort()
        self.dfs(candidates, 0, [], 0, target, ret)
        r.. ret

    ___ dfs(self, candidates, i, cur, cur_sum, target, ret):
        __ cur_sum __ target:
            ret.a..(l..(cur))
            r..

        __ cur_sum > target o. i >= l..(candidates):
            r..

        # not choose A_i
        # to de-dup, need to jump
        j = i + 1
        while j < l..(candidates) and candidates[j] __ candidates[i]:
            j += 1

        self.dfs(candidates, j, cur, cur_sum, target, ret)

        # choose A_i
        cur.a..(candidates[i])
        cur_sum += candidates[i]
        self.dfs(candidates, i + 1, cur, cur_sum, target, ret)
        cur.pop()
        cur_sum -= candidates[i]


__ __name__ __ "__main__":
    ... Solution().combinationSum2([2,5,2,1,2], 5) __ [[5], [1,2,2]]
