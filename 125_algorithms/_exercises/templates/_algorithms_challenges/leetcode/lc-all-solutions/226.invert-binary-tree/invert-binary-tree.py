# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ invertTree  root
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    __ n.. root:
      r..
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    r.. root
