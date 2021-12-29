'''
Created on Sep 25, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        __ not root: return []
        queue = [root]
        nextQueue = []
        sumVal = 0
        count = 0
        res = []
        while queue:
            node = queue.pop(0)
            sumVal += node.val
            count += 1
            __ node.left:
                nextQueue.append(node.left)
            __ node.right:
                nextQueue.append(node.right)
            __ not queue:
                res.append(float(sumVal)/count)
                sumVal = 0
                count = 0
                queue = nextQueue
                nextQueue = []
        return res
    
