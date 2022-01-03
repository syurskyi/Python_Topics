# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution(object):
    ___ lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        w.... root:
            __ root.val > p.val a.. root.val > q.val:
                root = root.left
            ____ root.val < p.val a.. root.val < q.val:
                root = root.right
            ____:
                r.. root
