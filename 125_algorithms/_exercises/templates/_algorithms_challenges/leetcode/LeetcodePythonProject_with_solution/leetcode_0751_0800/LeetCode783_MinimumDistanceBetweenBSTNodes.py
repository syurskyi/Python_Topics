'''
Created on Apr 9, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack    # list
        w.... root:
            stack.a..(root)
            root = root.left
        prev = float('-inf')
        res = float('inf')
        w.... stack:
            node = stack.pop()
            res = m..(res, node.val-prev)
            prev = node.val
            node0 = node.right
            w.... node0:
                stack.a..(node0)
                node0 = node0.left
        r.. res
