# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ flatten  root
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """

    ___ dfs(root
      __ n.. root:
        r.. root

      left = dfs(root.left)
      right = dfs(root.right)

      __ n.. left a.. n.. right:
        r.. root

      __ right __ N..
        root.right = root.left
        root.left = N..
        r.. left

      __ n.. left:
        r.. right

      tmp = root.right
      root.right = root.left
      root.left = N..
      left.right = tmp
      r.. right

    dfs(root)
