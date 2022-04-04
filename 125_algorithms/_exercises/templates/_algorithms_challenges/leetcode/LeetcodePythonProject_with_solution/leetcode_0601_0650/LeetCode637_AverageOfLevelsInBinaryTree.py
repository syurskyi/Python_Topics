'''
Created on Sep 25, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x
        val = x
        left = N..
        right = N..

c_ Solution(o..
    ___ averageOfLevels  root
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
            node = queue.p.. 0)
            sumVal += node.val
            count += 1
            __ node.left:
                nextQueue.a..(node.left)
            __ node.right:
                nextQueue.a..(node.right)
            __ n.. queue:
                res.a..(f__(sumVal)/count)
                sumVal = 0
                count = 0
                queue = nextQueue
                nextQueue    # list
        r.. res
    
