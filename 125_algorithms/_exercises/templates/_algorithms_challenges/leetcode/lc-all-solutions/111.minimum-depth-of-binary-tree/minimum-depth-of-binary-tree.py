# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ minDepth  root
    """
    :type root: TreeNode
    :rtype: int
    """
    __ n.. root:
      r.. 0
    left = minDepth(root.left)
    right = minDepth(root.right)
    __ n.. left a.. n.. right:
      r.. 1
    ____ n.. left:
      r.. right + 1
    ____ n.. right:
      r.. left + 1
    ____
      r.. m..(left, right) + 1
