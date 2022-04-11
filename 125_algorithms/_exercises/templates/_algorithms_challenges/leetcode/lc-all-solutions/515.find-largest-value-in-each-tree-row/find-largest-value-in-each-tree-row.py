# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ largestValues  root
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ans    # list
    d    # dict

    ___ dfs(root, h, d
      __ root:
        dfs(root.left, h + 1, d)
        dfs(root.right, h + 1, d)
        d[h] m..(d.g.. h, f__("-inf", root.val)

    dfs(root, 0, d)
    level 0
    w.... level __ d:
      ans += d[level],
      level += 1
    r.. ans
