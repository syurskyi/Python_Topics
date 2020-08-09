# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ diameterOfBinaryTree(self, root
    """
    :type root: TreeNode
    :rtype: int
    """
    self.ans = 0

    ___ dfs(root
      __ not root:
        r_ 0
      left = dfs(root.left)
      right = dfs(root.right)
      self.ans = max(self.ans, left + right)
      r_ max(left, right) + 1

    dfs(root)
    r_ self.ans
