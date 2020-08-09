# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None
from collections ______ deque


class Solution(object
  ___ rightSideView(self, root
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    ___ dfs(root, h
      __ root:
        __ h __ le.(ans
          ans.append(root.val)
        dfs(root.right, h + 1)
        dfs(root.left, h + 1)

    ans = []
    dfs(root, 0)
    r_ ans
