# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    __ n.. p o. n.. q:
      r.. p __ q
    r.. p.val __ q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
