# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
____ c.. _______ d..


c_ Solution(o..):
  ___ rightSideView  root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    ___ dfs(root, h):
      __ root:
        __ h __ l..(ans):
          ans.a..(root.val)
        dfs(root.right, h + 1)
        dfs(root.left, h + 1)

    ans    # list
    dfs(root, 0)
    r.. ans
