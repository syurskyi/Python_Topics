# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ findBottomLeftValue  root
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ dfs(root, h, w
      __ n.. root:
        r.. (f__("inf"), f__("inf"), N..)
      left dfs(root.left, h - 1, w - 1)
      right dfs(root.right, h - 1, w + 1)
      r.. m..((h, w, root.val), left, right)

    r.. dfs(root, 0, 0)[2]
