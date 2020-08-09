# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ getMinimumDifference(self, root
    """
    :type root: TreeNode
    :rtype: int
    """
    self.val = None
    self.ans = float("inf")

    ___ inorder(root
      __ not root:
        r_
      inorder(root.left)
      __ self.val is not None:
        self.ans = min(self.ans, abs(root.val - self.val))
      self.val = root.val
      inorder(root.right)

    inorder(root)
    r_ self.ans
