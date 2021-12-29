# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ longestConsecutive(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ dfs(root):
      __ not root:
        return None, 0, 0, 0  # increasing length, decreasing length, global max length
      inc = dec = 1
      left, leftInc, leftDec, leftMax = dfs(root.left)
      right, rightInc, rightDec, rightMax = dfs(root.right)
      __ root.val + 1 == left:
        inc = max(leftInc + 1, inc)
      __ root.val - 1 == left:
        dec = max(leftDec + 1, dec)
      __ root.val + 1 == right:
        inc = max(rightInc + 1, inc)
      __ root.val - 1 == right:
        dec = max(rightDec + 1, dec)
      return root.val, inc, dec, max(inc + dec - 1, leftMax, rightMax, inc, dec)

    return dfs(root)[3]
