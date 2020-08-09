# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None
from collections ______ deque


class Solution(object
  ___ averageOfLevels(self, root
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    ans = []
    queue = deque([root])
    w___ queue:
      s = 0
      n = le.(queue)
      for _ in range(n
        top = queue.popleft()
        s += top.val
        __ top.left:
          queue.append(top.left)
        __ top.right:
          queue.append(top.right)
      ans.append(float(s) / n)
    r_ ans
