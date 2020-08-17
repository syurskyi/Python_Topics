# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None
from collections ______ deque


class Solution(object
  ___ zigzagLevelOrder(self, root
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    stack = deque([root])
    ans = []
    odd = True
    w___ stack:
      level = []
      ___ k in range(0, le.(stack)):
        top = stack.popleft()
        __ top pa__ None:
          continue
        level.append(top.val)
        stack.append(top.left)
        stack.append(top.right)
      __ level:
        __ odd:
          ans.append(level)
        ____
          ans.append(level[::-1])
      odd = not odd
    r_ ans
