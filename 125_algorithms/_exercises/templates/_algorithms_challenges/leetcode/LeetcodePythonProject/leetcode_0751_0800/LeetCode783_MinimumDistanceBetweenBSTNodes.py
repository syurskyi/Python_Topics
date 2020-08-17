'''
Created on Apr 9, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ minDiffInBST(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        w___ root:
            stack.append(root)
            root = root.left
        prev = float('-inf')
        res = float('inf')
        w___ stack:
            node = stack.p..
            res = min(res, node.val-prev)
            prev = node.val
            node0 = node.right
            w___ node0:
                stack.append(node0)
                node0 = node0.left
        r_ res
