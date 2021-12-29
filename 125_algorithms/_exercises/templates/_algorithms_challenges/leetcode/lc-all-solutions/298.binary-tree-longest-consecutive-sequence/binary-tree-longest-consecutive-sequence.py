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

    ___ helper(root):
      __ not root:
        return (None, 0, 0)  # (val, consecutive len, max consecutive len)
      left, leftLen, maxLeftLen = helper(root.left)
      right, rightLen, maxRightLen = helper(root.right)
      ret = 1
      __ root.val + 1 == left:
        ret = leftLen + 1
      __ root.val + 1 == right:
        ret = max(ret, rightLen + 1)
      return (root.val, ret, max(maxLeftLen, maxRightLen, ret))

    return helper(root)[2]
