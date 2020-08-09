# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ maxPathSum(self, root
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ dfs(root
      __ not root: r_ (0, float("-inf"))
      (l, lm), (r, rm) = map(dfs, [root.left, root.right])
      r_ (max(root.val, root.val + max(l, r)), max(lm, rm, root.val + max(l, r), root.val, root.val + l + r))

    r_ dfs(root)[1]
