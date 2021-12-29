'''
Created on Mar 15, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ verticalOrder(self, root):
        __ n.. root: r.. []
        hashmap = {}
        result    # list
        queue = [(0, root)]
        minLevel, maxLevel = 0, 0
        while queue:
            level, node = queue.pop(0)
            maxLevel = max(maxLevel, level)
            minLevel = m..(minLevel, level)
            __ level n.. __ hashmap:
                hashmap[level] = [node.val]
            ____:
                hashmap[level].a..(node.val)
            __ node.left:
                queue.a..((level-1, node.left))
            __ node.right:
                queue.a..((level+1, node.right))
        ___ i __ r..(minLevel, maxLevel+1):
            result.a..(hashmap[i])
        r.. result
    
    