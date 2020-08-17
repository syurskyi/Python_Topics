# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ isSubtree(self, s, t
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """

    ___ serialize(root
      ans = []
      stack = [(root, 1)]
      w___ stack:
        node, p = stack.p..
        __ not node:
          ans.append("#")
          continue
        __ p __ 0:
          ans.append("|" + str(node.val))
        ____
          stack.append((node.right, 1))
          stack.append((node.left, 1))
          stack.append((node, 0))
      r_ ",".join(ans)

    r_ serialize(t) in serialize(s)
