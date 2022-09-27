# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ hasPathSum  root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        __ root is N..:
            r_ F..
        sum = sum - root.val
        __ sum __ 0 and root.left is N.. and root.right is N..:
            r_ T..
        # check left
        left = hasPathSum(root.left, sum)
        # check right
        right = hasPathSum(root.right, sum)
        r_ (left or right)
