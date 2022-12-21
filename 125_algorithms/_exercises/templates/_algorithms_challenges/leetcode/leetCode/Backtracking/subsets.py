"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
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

直接上递归，每条线都有两个决策：
1. 加上。
2. 不加。

beat 96%

测试地址：
https://leetcode.com/problems/subsets/description/

"""
c.. Solution o..
    ___ subsets  nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result   # list
        
        length = l..(nums)
        
        ___ makeSubsets(index, current_subsets
            __ index __ length:
                r_
            
            result.append(current_subsets+[nums[index]])
            
            makeSubsets(index+1, current_subsets+[nums[index]])
            makeSubsets(index+1, current_subsets)


        makeSubsets(0, [])
        
        r_ result+[[]]
        