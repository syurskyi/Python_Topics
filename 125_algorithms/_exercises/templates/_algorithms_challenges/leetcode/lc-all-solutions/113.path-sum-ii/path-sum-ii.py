# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..):
  ___ pathSum  root, s..):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """

    ___ dfs(root, s, path, res):
      __ root:
        path.a..(root.val)
        s -= root.val
        left = dfs(root.left, s, path, res)
        right = dfs(root.right, s, path, res)
        __ n.. left a.. n.. right a.. s __ 0:
          res.a..(path + [])
        path.pop()
        r.. T..

    res    # list
    dfs(root, s.., [], res)
    r.. res
