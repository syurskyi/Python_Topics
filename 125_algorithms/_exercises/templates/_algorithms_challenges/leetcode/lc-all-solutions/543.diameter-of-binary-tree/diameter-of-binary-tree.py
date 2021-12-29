# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.ans = 0

    ___ dfs(root):
      __ n.. root:
        r.. 0
      left = dfs(root.left)
      right = dfs(root.right)
      self.ans = max(self.ans, left + right)
      r.. max(left, right) + 1

    dfs(root)
    r.. self.ans
