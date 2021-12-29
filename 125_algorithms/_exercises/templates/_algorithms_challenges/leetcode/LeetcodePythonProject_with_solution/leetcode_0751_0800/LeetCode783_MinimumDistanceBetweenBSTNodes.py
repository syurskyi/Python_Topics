'''
Created on Apr 9, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        while root:
            stack.append(root)
            root = root.left
        prev = float('-inf')
        res = float('inf')
        while stack:
            node = stack.pop()
            res = min(res, node.val-prev)
            prev = node.val
            node0 = node.right
            while node0:
                stack.append(node0)
                node0 = node0.left
        return res
