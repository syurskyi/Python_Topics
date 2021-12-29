# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ upsideDownBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    __ n.. root:
      r..

    left = self.upsideDownBinaryTree(root.left)
    right = self.upsideDownBinaryTree(root.right)
    __ root.left:
      root.left.right = root
      root.left.left = root.right
      root.left = root.right = N..
    r.. left __ left ____ root
