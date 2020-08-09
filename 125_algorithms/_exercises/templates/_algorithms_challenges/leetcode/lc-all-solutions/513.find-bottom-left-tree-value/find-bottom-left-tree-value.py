# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ findBottomLeftValue(self, root
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ dfs(root, h, w
      __ not root:
        r_ (float("inf"), float("inf"), None)
      left = dfs(root.left, h - 1, w - 1)
      right = dfs(root.right, h - 1, w + 1)
      r_ min((h, w, root.val), left, right)

    r_ dfs(root, 0, 0)[2]
