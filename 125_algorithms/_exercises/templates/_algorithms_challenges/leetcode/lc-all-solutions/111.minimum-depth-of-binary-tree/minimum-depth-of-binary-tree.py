# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    __ not root:
      return 0
    left = self.minDepth(root.left)
    right = self.minDepth(root.right)
    __ not left and not right:
      return 1
    elif not left:
      return right + 1
    elif not right:
      return left + 1
    else:
      return min(left, right) + 1
