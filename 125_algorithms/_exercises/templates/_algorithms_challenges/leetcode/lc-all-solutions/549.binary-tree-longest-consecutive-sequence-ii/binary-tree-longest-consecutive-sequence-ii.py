# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ longestConsecutive(self, root
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ dfs(root
      __ not root:
        r_ None, 0, 0, 0  # increasing length, decreasing length, global max length
      inc = dec = 1
      left, leftInc, leftDec, leftMax = dfs(root.left)
      right, rightInc, rightDec, rightMax = dfs(root.right)
      __ root.val + 1 __ left:
        inc = ma.(leftInc + 1, inc)
      __ root.val - 1 __ left:
        dec = ma.(leftDec + 1, dec)
      __ root.val + 1 __ right:
        inc = ma.(rightInc + 1, inc)
      __ root.val - 1 __ right:
        dec = ma.(rightDec + 1, dec)
      r_ root.val, inc, dec, ma.(inc + dec - 1, leftMax, rightMax, inc, dec)

    r_ dfs(root)[3]
