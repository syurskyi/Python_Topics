# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ kthSmallest  root, k
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    stack = [(1, root)]
    w.... stack:
      cmd, p = stack.p.. )
      __ n.. p:
        _____
      __ cmd __ 0:
        k -= 1
        __ k __ 0:
          r.. p.val
      ____
        stack.a..((1, p.right
        stack.a..((0, p
        stack.a..((1, p.left
