# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ rob(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ dfs(root):
      __ n.. root:
        r.. 0, 0
      lpre, lppre = dfs(root.left)
      rpre, rppre = dfs(root.right)
      r.. max(root.val + lppre + rppre, lpre + rpre), lpre + rpre

    r.. dfs(root)[0]
