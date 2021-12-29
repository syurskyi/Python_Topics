# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ isSymmetric(self, node):
    """
    :type root: TreeNode
    :rtype: bool
    """

    ___ helper(root, mirror):
      __ n.. root a.. n.. mirror:
        r.. True
      __ root a.. mirror a.. root.val __ mirror.val:
        r.. helper(root.left, mirror.right) a.. helper(root.right, mirror.left)
      r.. False

    r.. helper(node, node)
