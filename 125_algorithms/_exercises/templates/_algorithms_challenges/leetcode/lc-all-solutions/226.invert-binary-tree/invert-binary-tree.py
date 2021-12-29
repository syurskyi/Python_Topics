# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    __ n.. root:
      r..
    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    r.. root
