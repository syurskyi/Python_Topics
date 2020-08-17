# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ deleteNode(self, root, key
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """

    ___ delete(root, pre
      __ root.right:
        p = root.right
        w___ p.left:
          p = p.left
        p.left = root.left
      __ root pa__ pre.left:
        pre.left = root.right or root.left
      __ root pa__ pre.right:
        pre.right = root.right or root.left
      root.left = None

    __ not root:
      r_ root
    pre = dummy = TreeNode(float("inf"))
    dummy.left = root
    p = dummy
    w___ p:
      __ key > p.val:
        pre = p
        p = p.right
      ____ key < p.val:
        pre = p
        p = p.left
      ____
        delete(p, pre)
        break
    r_ dummy.left
