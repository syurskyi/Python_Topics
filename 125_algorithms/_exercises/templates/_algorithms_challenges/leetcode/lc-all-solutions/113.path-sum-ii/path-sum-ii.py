# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ pathSum  root, s..
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """

    ___ dfs(root, s, p.., res
      __ root:
        p...a..(root.val)
        s -_ root.val
        left dfs(root.left, s, p.., res)
        right dfs(root.right, s, p.., res)
        __ n.. left a.. n.. right a.. s __ 0:
          res.a..(p.. + [])
        p...p.. )
        r.. T..

    res    # list
    dfs(root, s.., [], res)
    r.. res
