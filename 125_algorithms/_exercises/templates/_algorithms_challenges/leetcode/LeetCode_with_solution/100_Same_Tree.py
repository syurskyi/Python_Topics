# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ isSameTree  p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        __ p __ q:
            r_ T..
        try:
            left = right = T..
            __ p.val __ q.val:
                left = isSameTree(p.left, q.left)
                right = isSameTree(p.right, q.right)
                r_ (left and right)
        except:
            r_ F..
        r_ F..