'''
Created on Sep 25, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ averageOfLevels  root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        __ n.. root: r.. []
        queue = [root]
        nextQueue    # list
        sumVal = 0
        count = 0
        res    # list
        w.... queue:
            node = queue.pop(0)
            sumVal += node.val
            count += 1
            __ node.left:
                nextQueue.a..(node.left)
            __ node.right:
                nextQueue.a..(node.right)
            __ n.. queue:
                res.a..(float(sumVal)/count)
                sumVal = 0
                count = 0
                queue = nextQueue
                nextQueue    # list
        r.. res
    
