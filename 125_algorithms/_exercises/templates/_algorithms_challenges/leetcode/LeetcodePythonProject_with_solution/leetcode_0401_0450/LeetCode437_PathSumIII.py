'''
Created on Apr 16, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ pathSum(self, root, sumVal):
        __ not root: return 0
        return self.helper(root, sumVal) +\
            self.pathSum(root.left, sumVal)+\
            self.pathSum(root.right, sumVal)
    
    ___ helper(self, root, sumVal):
        __ not root: return 0
        __ root.val == sumVal:
            res = 1
        else:
            res = 0
        res += self.helper(root.left, sumVal-root.val)
        res += self.helper(root.right, sumVal-root.val)
        return res
    
    ___ pathSum_second(self, root, sumVal):
        hashmap = {0:1}
        return self.dfs(root, 0, sumVal, hashmap)
    
    ___ dfs(self, root, sumVal, target, hashmap):
        __ not root: return 0
        sumVal += root.val
        res = hashmap.get(sumVal-target, 0)
        hashmap[sumVal] = hashmap.get(sumVal, 0)+1
        res += self.dfs(root.left, sumVal, target, hashmap)
        res += self.dfs(root.right, sumVal, target, hashmap)
        hashmap[sumVal] = hashmap[sumVal]-1
        return res
