# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
  ___ zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    stack = deque([root])
    ans = []
    odd = True
    while stack:
      level = []
      for k in range(0, len(stack)):
        top = stack.popleft()
        __ top is None:
          continue
        level.append(top.val)
        stack.append(top.left)
        stack.append(top.right)
      __ level:
        __ odd:
          ans.append(level)
        else:
          ans.append(level[::-1])
      odd = not odd
    return ans
