# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ isSymmetric  root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ root is N..:
            r_ True
        r_ mirrorVisit(root.left, root.right)

    ___ mirrorVisit  left, right):
        __ left is N.. and right is N..:
            r_ True
        try:
            __ left.val __ right.val:
                __ mirrorVisit(left.left, right.right) and mirrorVisit(left.right, right.left):
                    r_ True
            r_ False
        except:
            r_ False