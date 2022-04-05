#!/usr/bin/python3
"""
Given a set of candidate numbers (candidates) (without duplicates) and a target
number (target), find all unique combinations in candidates where the candidate
numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of
times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
____ t___ _______ L..


c_ Solution:
    ___ combinationSum  candidates: L..[i..], target: i..) __ L..[L..[i..]]:
        ret    # list
        dfs(candidates, 0, [], 0, target, ret)
        r.. ret

    ___ dfs  candidates, i, cur, cur_sum, target, ret
        __ cur_sum __ target:
            ret.a..(l..(cur
            r..
            
        __ cur_sum > target o. i >_ l..(candidates
            r..

        # not choose A_i
        dfs(candidates, i + 1, cur, cur_sum, target, ret)

        # choose A_i
        cur.a..(candidates[i])
        cur_sum += candidates[i]
        dfs(candidates, i, cur, cur_sum, target, ret)
        cur.p.. )
        cur_sum -_ candidates[i]
