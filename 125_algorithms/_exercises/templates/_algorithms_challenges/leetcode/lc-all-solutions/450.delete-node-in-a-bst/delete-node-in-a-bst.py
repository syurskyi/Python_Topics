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
        while p.left:
          p = p.left
        p.left = root.left
      __ root is pre.left:
        pre.left = root.right or root.left
      __ root is pre.right:
        pre.right = root.right or root.left
      root.left = None

    __ not root:
      return root
    pre = dummy = TreeNode(float("inf"))
    dummy.left = root
    p = dummy
    while p:
      __ key > p.val:
        pre = p
        p = p.right
      elif key < p.val:
        pre = p
        p = p.left
      else:
        delete(p, pre)
        break
    return dummy.left
