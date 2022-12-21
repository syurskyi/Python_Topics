# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ hasPathSum  root, s..
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        __ root is N..:
            r_ F..
        s.. = s.. - root.val
        __ s.. __ 0 and root.left is N.. and root.right is N..:
            r_ T..
        # check left
        left = hasPathSum(root.left, s..)
        # check right
        right = hasPathSum(root.right, s..)
        r_ (left or right)
