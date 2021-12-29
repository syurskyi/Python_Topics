'''
Created on Apr 16, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ pathSum(self, root, sumVal):
        __ n.. root: r.. 0
        r.. self.helper(root, sumVal) +\
            self.pathSum(root.left, sumVal)+\
            self.pathSum(root.right, sumVal)
    
    ___ helper(self, root, sumVal):
        __ n.. root: r.. 0
        __ root.val __ sumVal:
            res = 1
        ____:
            res = 0
        res += self.helper(root.left, sumVal-root.val)
        res += self.helper(root.right, sumVal-root.val)
        r.. res
    
    ___ pathSum_second(self, root, sumVal):
        hashmap = {0:1}
        r.. self.dfs(root, 0, sumVal, hashmap)
    
    ___ dfs(self, root, sumVal, target, hashmap):
        __ n.. root: r.. 0
        sumVal += root.val
        res = hashmap.get(sumVal-target, 0)
        hashmap[sumVal] = hashmap.get(sumVal, 0)+1
        res += self.dfs(root.left, sumVal, target, hashmap)
        res += self.dfs(root.right, sumVal, target, hashmap)
        hashmap[sumVal] = hashmap[sumVal]-1
        r.. res
