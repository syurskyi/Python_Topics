# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution(o..
    ___ buildTree  P, I
        """
        :type P: List[int]
        :type I: List[int]
        :rtype: TreeNode
        """
        __ n.. P o. n.. I:
            r..

        i = I.i.. P.pop(0))
        node = TreeNode(I[i])
        node.left = buildTree(P, I[:i])
        node.right = buildTree(P, I[i + 1:])
        r.. node
