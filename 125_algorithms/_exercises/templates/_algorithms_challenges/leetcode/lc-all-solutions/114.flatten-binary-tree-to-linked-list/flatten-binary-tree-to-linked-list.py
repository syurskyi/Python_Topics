# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ flatten(self, root
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """

    ___ dfs(root
      __ not root:
        r_ root

      left = dfs(root.left)
      right = dfs(root.right)

      __ not left and not right:
        r_ root

      __ right pa__ None:
        root.right = root.left
        root.left = None
        r_ left

      __ not left:
        r_ right

      tmp = root.right
      root.right = root.left
      root.left = None
      left.right = tmp
      r_ right

    dfs(root)
