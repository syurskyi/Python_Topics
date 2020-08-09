# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ largestValues(self, root
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ans = []
    d = {}

    ___ dfs(root, h, d
      __ root:
        dfs(root.left, h + 1, d)
        dfs(root.right, h + 1, d)
        d[h] = max(d.get(h, float("-inf")), root.val)

    dfs(root, 0, d)
    level = 0
    w___ level in d:
      ans += d[level],
      level += 1
    r_ ans
