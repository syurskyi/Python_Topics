'''
Created on May 17, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ n.. root: r.. []
        queue = [root]
        nextQueue    # list
        res = [root.val]
        while queue:
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
