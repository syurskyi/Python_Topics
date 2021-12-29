# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ deleteNode(self, root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """

    ___ delete(root, pre):
      __ root.right:
        p = root.right
        w.... p.left:
          p = p.left
        p.left = root.left
      __ root __ pre.left:
        pre.left = root.right o. root.left
      __ root __ pre.right:
        pre.right = root.right o. root.left
      root.left = N..

    __ n.. root:
      r.. root
    pre = dummy = TreeNode(float("inf"))
    dummy.left = root
    p = dummy
    w.... p:
      __ key > p.val:
        pre = p
        p = p.right
      ____ key < p.val:
        pre = p
        p = p.left
      ____:
        delete(p, pre)
        break
    r.. dummy.left
