# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object
    ___ buildTree(self, P, I
        """
        :type P: List[int]
        :type I: List[int]
        :rtype: TreeNode
        """
        __ not P or not I:
            r_

        i = I.index(P.pop(0))
        node = TreeNode(I[i])
        node.left = self.buildTree(P, I[:i])
        node.right = self.buildTree(P, I[i + 1:])
        r_ node
