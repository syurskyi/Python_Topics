# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    ___ dfs(p):
      __ not p:
        return 0

      left = dfs(p.left)
      right = dfs(p.right)
      __ left == -1 or right == -1:
        return -1
      __ abs(left - right) > 1:
        return -1
      return 1 + max(left, right)

    __ dfs(root) == -1:
      return False
    return True
