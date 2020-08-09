'''
Created on May 17, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ rightSideView(self, root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ not root: r_ []
        queue = [root]
        nextQueue = []
        res = [root.val]
        w___ queue:
            node = queue.pop(0)
            __ node.left:
                nextQueue.append(node.left)
            __ node.right:
                nextQueue.append(node.right)
            __ not queue:
                __ nextQueue:
                    res.append(nextQueue[-1].val)
                    queue = nextQueue
                    nextQueue = []
        r_ res
