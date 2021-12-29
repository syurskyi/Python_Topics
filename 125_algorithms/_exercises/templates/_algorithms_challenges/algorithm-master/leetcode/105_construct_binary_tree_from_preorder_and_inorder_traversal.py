# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    ___ buildTree(self, P, I):
        """
        :type P: List[int]
        :type I: List[int]
        :rtype: TreeNode
        """
        __ n.. P o. n.. I:
            r..

        i = I.index(P.pop(0))
        node = TreeNode(I[i])
        node.left = self.buildTree(P, I[:i])
        node.right = self.buildTree(P, I[i + 1:])
        r.. node
