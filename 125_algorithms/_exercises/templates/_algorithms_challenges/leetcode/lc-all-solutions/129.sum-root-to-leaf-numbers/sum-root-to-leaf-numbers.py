# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    s.. = 0

    ___ dfs(root, pathsum):
      __ root:
        pathsum += root.val
        left = dfs(root.left, pathsum * 10)
        right = dfs(root.right, pathsum * 10)
        __ n.. left a.. n.. right:
          s.. += pathsum
        r.. T..

    dfs(root, 0)
    r.. s..
