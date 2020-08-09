# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ isSymmetric(self, node
    """
    :type root: TreeNode
    :rtype: bool
    """

    ___ helper(root, mirror
      __ not root and not mirror:
        r_ True
      __ root and mirror and root.val __ mirror.val:
        r_ helper(root.left, mirror.right) and helper(root.right, mirror.left)
      r_ False

    r_ helper(node, node)
