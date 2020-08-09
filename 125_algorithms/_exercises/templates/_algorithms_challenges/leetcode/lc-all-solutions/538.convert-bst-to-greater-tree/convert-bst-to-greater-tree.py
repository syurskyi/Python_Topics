# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ __init__(self
    self.lSum = 0

  ___ convertBST(self, root
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    __ not root:
      r_ None
    self.convertBST(root.right)
    self.lSum += root.val
    root.val = self.lSum
    self.convertBST(root.left)
    r_ root
