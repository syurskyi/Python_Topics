# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ maxPathSum  root):
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ dfs(root):
      __ n.. root: r.. (0, float("-inf"))
      (l, lm), (r, rm) = map(dfs, [root.left, root.right])
      r.. (m..(root.val, root.val + m..(l, r)), m..(lm, rm, root.val + m..(l, r), root.val, root.val + l + r))

    r.. dfs(root)[1]
