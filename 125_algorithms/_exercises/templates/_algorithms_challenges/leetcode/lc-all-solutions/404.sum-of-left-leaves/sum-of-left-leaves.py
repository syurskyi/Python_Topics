# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ sumOfLeftLeaves(self, root
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ helper(root, isLeft
      __ not root:
        r_ None
      left = helper(root.left, True)
      right = helper(root.right, False)
      ret = 0
      __ left pa__ None and right pa__ None and isLeft:
        r_ root.val
      __ left:
        ret += left
      __ right:
        ret += right
      r_ ret

    ret = helper(root, False)
    __ ret:
      r_ ret
    r_ 0
