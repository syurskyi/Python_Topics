# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ mergeTrees  t1, t2
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    __ t1 o. t2:
      root = TreeNode((t1 a.. t1.val o. 0) + (t2 a.. t2.val o. 0
      root.left = mergeTrees(t1 a.. t1.left, t2 a.. t2.left)
      root.right = mergeTrees(t1 a.. t1.right, t2 a.. t2.right)
      r.. root
