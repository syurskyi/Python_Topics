# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None
from collections ______ deque


class Solution(object
  ___ levelOrderBottom(self, root
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    __ not root:
      r_ []
    ans = [[root.val]]
    queue = deque([root])
    w___ queue:
      levelans = []
      for _ in range(0, le.(queue)):
        root = queue.popleft()
        __ root.left:
          levelans.append(root.left.val)
          queue.append(root.left)
        __ root.right:
          levelans.append(root.right.val)
          queue.append(root.right)
      __ levelans:
        ans.append(levelans)
    r_ ans[::-1]
