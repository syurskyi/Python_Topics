# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ countUnivalSubtrees  root):
    """
    :type root: TreeNode
    :rtype: int
    """
    count = 0

    ___ dfs(root, pv):
      __ n.. root:
        r.. T..
      left = dfs(root.left, root.val)
      right = dfs(root.right, root.val)
      __ left a.. right:
        count += 1
        __ root.val __ pv:
          r.. T..
      r.. F..

    __ root:
      dfs(root, root.val)
    r.. count
