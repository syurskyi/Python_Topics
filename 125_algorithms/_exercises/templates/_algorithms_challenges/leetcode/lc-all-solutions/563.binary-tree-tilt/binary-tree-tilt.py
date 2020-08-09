# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ findTilt(self, root
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ dfs(root
      __ not root:
        r_ 0, 0  # sum, tilt sum

      leftSum, leftTilt = dfs(root.left)
      rightSum, rightTilt = dfs(root.right)

      r_ leftSum + root.val + rightSum, abs(leftSum - rightSum) + leftTilt + rightTilt

    r_ dfs(root)[1]
