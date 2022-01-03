'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res    # list
        __ n.. root: r.. res
        queue, nextQueue, elem = [root], [], []
        order = T..
        w.... queue:
            node = queue.pop(0)
            elem.a..(node.val)
            __ node.left:
                nextQueue.a..(node.left)
            __ node.right:
                nextQueue.a..(node.right)
            __ n.. queue:
                __ n.. order:
                    res.a..(elem[::-1])
                ____:
                    res.a..(elem)
                elem    # list
                queue = nextQueue
                nextQueue    # list
                order = n.. order
        r.. res
