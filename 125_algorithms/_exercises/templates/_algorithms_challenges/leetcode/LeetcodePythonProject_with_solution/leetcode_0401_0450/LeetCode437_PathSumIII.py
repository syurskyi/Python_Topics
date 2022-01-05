'''
Created on Apr 16, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ pathSum  root, sumVal):
        __ n.. root: r.. 0
        r.. helper(root, sumVal) +\
            pathSum(root.left, sumVal)+\
            pathSum(root.right, sumVal)
    
    ___ helper  root, sumVal):
        __ n.. root: r.. 0
        __ root.val __ sumVal:
            res = 1
        ____:
            res = 0
        res += helper(root.left, sumVal-root.val)
        res += helper(root.right, sumVal-root.val)
        r.. res
    
    ___ pathSum_second  root, sumVal):
        hashmap = {0:1}
        r.. dfs(root, 0, sumVal, hashmap)
    
    ___ dfs  root, sumVal, target, hashmap):
        __ n.. root: r.. 0
        sumVal += root.val
        res = hashmap.get(sumVal-target, 0)
        hashmap[sumVal] = hashmap.get(sumVal, 0)+1
        res += dfs(root.left, sumVal, target, hashmap)
        res += dfs(root.right, sumVal, target, hashmap)
        hashmap[sumVal] = hashmap[sumVal]-1
        r.. res
