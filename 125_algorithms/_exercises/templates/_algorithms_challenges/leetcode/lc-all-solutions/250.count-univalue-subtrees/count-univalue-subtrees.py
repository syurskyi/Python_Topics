# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ countUnivalSubtrees(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.count = 0

    ___ dfs(root, pv):
      __ n.. root:
        r.. True
      left = dfs(root.left, root.val)
      right = dfs(root.right, root.val)
      __ left and right:
        self.count += 1
        __ root.val __ pv:
          r.. True
      r.. False

    __ root:
      dfs(root, root.val)
    r.. self.count
