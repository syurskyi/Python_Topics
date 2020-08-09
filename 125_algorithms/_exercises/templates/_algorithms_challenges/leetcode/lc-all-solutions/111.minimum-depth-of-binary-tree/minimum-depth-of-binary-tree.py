# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ minDepth(self, root
    """
    :type root: TreeNode
    :rtype: int
    """
    __ not root:
      r_ 0
    left = self.minDepth(root.left)
    right = self.minDepth(root.right)
    __ not left and not right:
      r_ 1
    ____ not left:
      r_ right + 1
    ____ not right:
      r_ left + 1
    ____
      r_ min(left, right) + 1
