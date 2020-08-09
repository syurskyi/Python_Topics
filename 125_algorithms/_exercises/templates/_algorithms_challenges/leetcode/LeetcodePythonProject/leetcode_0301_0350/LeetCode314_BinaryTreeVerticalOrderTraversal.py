'''
Created on Mar 15, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution(object
    ___ verticalOrder(self, root
        __ not root: r_ []
        hashmap = {}
        result = []
        queue = [(0, root)]
        minLevel, maxLevel = 0, 0
        w___ queue:
            level, node = queue.pop(0)
            maxLevel = max(maxLevel, level)
            minLevel = min(minLevel, level)
            __ level not in hashmap:
                hashmap[level] = [node.val]
            ____
                hashmap[level].append(node.val)
            __ node.left:
                queue.append((level-1, node.left))
            __ node.right:
                queue.append((level+1, node.right))
        ___ i in range(minLevel, maxLevel+1
            result.append(hashmap[i])
        r_ result
    
    