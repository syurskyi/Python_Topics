'''
Created on May 17, 2018

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ rightSideView  root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ n.. root: r.. []
        queue = [root]
        nextQueue    # list
        res = [root.val]
        w.... queue:
            node = queue.pop(0)
            __ node.left:
                nextQueue.a..(node.left)
            __ node.right:
                nextQueue.a..(node.right)
            __ n.. queue:
                __ nextQueue:
                    res.a..(nextQueue[-1].val)
                    queue = nextQueue
                    nextQueue    # list
        r.. res
