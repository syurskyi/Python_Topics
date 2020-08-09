# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ isValidBST(self, root
    """
    :type root: TreeNode
    :rtype: bool
    """
    prev = -float("inf")
    stack = [(1, root)]
    w___ stack:
      p = stack.pop()
      __ not p[1]:
        continue
      __ p[0] __ 0:
        __ p[1].val <= prev:
          r_ False
        prev = p[1].val
      ____
        stack.append((1, p[1].right))
        stack.append((0, p[1]))
        stack.append((1, p[1].left))
    r_ True
