# Combinations Sum II
# Question: Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# Each number in C may only be used once in the combination.
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# A solution set is: [1, 7] ; [1, 2, 5] ; [2, 6] ; [1, 1, 6]
# Solutions:


c_ Solution:
    ___ combinationSum2(self, candidates, target):
        __ not candidates:
            r_   # list
        candidates.sort()
        result _   # list
        combination(candidates, target,   # list, result)
        r_ result
    ___ combination(self, candidates, target, current, result):
        s _ su.(current) __ current ____ 0
        __ s > target:
            r_
        elif s __ target:
            result.ap..(current)
            r_
        ____
            i _ 0
            while i < le.(candidates):
                combination(candidates[i + 1:], target, current + [candidates[i]], result)
                while i + 1 < le.(candidates) an. candidates[i] __ candidates[i + 1]:
                    i +_ 1
            i +_ 1


Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)