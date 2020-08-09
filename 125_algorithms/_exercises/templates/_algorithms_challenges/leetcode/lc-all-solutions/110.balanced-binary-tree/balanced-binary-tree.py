# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ isBalanced(self, root
    """
    :type root: TreeNode
    :rtype: bool
    """

    ___ dfs(p
      __ not p:
        r_ 0

      left = dfs(p.left)
      right = dfs(p.right)
      __ left __ -1 or right __ -1:
        r_ -1
      __ abs(left - right) > 1:
        r_ -1
      r_ 1 + max(left, right)

    __ dfs(root) __ -1:
      r_ False
    r_ True
