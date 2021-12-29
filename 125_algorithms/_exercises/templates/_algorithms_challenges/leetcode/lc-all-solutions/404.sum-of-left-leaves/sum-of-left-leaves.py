# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ helper(root, isLeft):
      __ not root:
        return None
      left = helper(root.left, True)
      right = helper(root.right, False)
      ret = 0
      __ left is None and right is None and isLeft:
        return root.val
      __ left:
        ret += left
      __ right:
        ret += right
      return ret

    ret = helper(root, False)
    __ ret:
      return ret
    return 0
