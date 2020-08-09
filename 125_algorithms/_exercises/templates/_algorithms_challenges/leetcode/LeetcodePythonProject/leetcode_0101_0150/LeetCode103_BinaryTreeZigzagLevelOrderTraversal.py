'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution(object
    ___ zigzagLevelOrder(self, root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        __ not root: r_ res
        queue, nextQueue, elem = [root], [], []
        order = True
        w___ queue:
            node = queue.pop(0)
            elem.append(node.val)
            __ node.left:
                nextQueue.append(node.left)
            __ node.right:
                nextQueue.append(node.right)
            __ not queue:
                __ not order:
                    res.append(elem[::-1])
                ____
                    res.append(elem)
                elem = []
                queue = nextQueue
                nextQueue = []
                order = not order
        r_ res
