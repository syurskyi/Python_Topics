# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """

    ___ serialize(root):
      ans    # list
      stack = [(root, 1)]
      w.... stack:
        node, p = stack.pop()
        __ n.. node:
          ans.a..("#")
          continue
        __ p __ 0:
          ans.a..("|" + s..(node.val))
        ____:
          stack.a..((node.right, 1))
          stack.a..((node.left, 1))
          stack.a..((node, 0))
      r.. ",".j..(ans)

    r.. serialize(t) __ serialize(s)
