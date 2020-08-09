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

    ___ helper(root
      __ not root:
        r_ (None, 0, 0)  # (val, consecutive le., max consecutive le.)
      left, leftLen, maxLeftLen = helper(root.left)
      right, rightLen, maxRightLen = helper(root.right)
      ret = 1
      __ root.val + 1 __ left:
        ret = leftLen + 1
      __ root.val + 1 __ right:
        ret = max(ret, rightLen + 1)
      r_ (root.val, ret, max(maxLeftLen, maxRightLen, ret))

    r_ helper(root)[2]
