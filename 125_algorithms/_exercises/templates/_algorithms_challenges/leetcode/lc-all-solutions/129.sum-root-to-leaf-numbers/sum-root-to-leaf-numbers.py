# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.sum = 0

    ___ dfs(root, pathsum):
      __ root:
        pathsum += root.val
        left = dfs(root.left, pathsum * 10)
        right = dfs(root.right, pathsum * 10)
        __ not left and not right:
          self.sum += pathsum
        return True

    dfs(root, 0)
    return self.sum
