# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ isSymmetric  node):
    """
    :type root: TreeNode
    :rtype: bool
    """

    ___ helper(root, mirror):
      __ n.. root a.. n.. mirror:
        r.. T..
      __ root a.. mirror a.. root.val __ mirror.val:
        r.. helper(root.left, mirror.right) a.. helper(root.right, mirror.left)
      r.. F..

    r.. helper(node, node)
