# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    __ n.. root:
      r.. 0
    r.. max(maxDepth(root.left), maxDepth(root.right)) + 1
