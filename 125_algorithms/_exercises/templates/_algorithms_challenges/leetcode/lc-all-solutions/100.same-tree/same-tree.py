# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    __ n.. p o. n.. q:
      r.. p __ q
    r.. p.val __ q.val a.. isSameTree(p.left, q.left) a.. isSameTree(p.right, q.right)
