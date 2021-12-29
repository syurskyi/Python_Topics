# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ flatten(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """

    ___ dfs(root):
      __ not root:
        return root

      left = dfs(root.left)
      right = dfs(root.right)

      __ not left and not right:
        return root

      __ right is None:
        root.right = root.left
        root.left = None
        return left

      __ not left:
        return right

      tmp = root.right
      root.right = root.left
      root.left = None
      left.right = tmp
      return right

    dfs(root)
