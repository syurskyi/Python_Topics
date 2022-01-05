# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ longestConsecutive  root):
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ dfs(root):
      __ n.. root:
        r.. N.., 0, 0, 0  # increasing length, decreasing length, global max length
      inc = dec = 1
      left, leftInc, leftDec, leftMax = dfs(root.left)
      right, rightInc, rightDec, rightMax = dfs(root.right)
      __ root.val + 1 __ left:
        inc = m..(leftInc + 1, inc)
      __ root.val - 1 __ left:
        dec = m..(leftDec + 1, dec)
      __ root.val + 1 __ right:
        inc = m..(rightInc + 1, inc)
      __ root.val - 1 __ right:
        dec = m..(rightDec + 1, dec)
      r.. root.val, inc, dec, m..(inc + dec - 1, leftMax, rightMax, inc, dec)

    r.. dfs(root)[3]
