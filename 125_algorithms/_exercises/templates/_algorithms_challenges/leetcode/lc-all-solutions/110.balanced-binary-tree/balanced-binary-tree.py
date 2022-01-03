# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    ___ dfs(p):
      __ n.. p:
        r.. 0

      left = dfs(p.left)
      right = dfs(p.right)
      __ left __ -1 o. right __ -1:
        r.. -1
      __ abs(left - right) > 1:
        r.. -1
      r.. 1 + max(left, right)

    __ dfs(root) __ -1:
      r.. F..
    r.. T..
