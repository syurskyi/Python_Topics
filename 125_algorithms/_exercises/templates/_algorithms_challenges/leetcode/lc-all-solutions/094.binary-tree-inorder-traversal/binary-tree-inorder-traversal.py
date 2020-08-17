# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ inorderTraversal(self, root
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res, stack = [], [(1, root)]
    w___ stack:
      p = stack.p..
      __ not p[1]: continue
      stack.extend([(1, p[1].right), (0, p[1]), (1, p[1].left)]) __ p[0] != 0 else res.append(p[1].val)
    r_ res
