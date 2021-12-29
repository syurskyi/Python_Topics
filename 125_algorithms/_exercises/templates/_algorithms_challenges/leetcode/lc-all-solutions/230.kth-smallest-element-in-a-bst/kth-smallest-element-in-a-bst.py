# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    stack = [(1, root)]
    while stack:
      cmd, p = stack.pop()
      __ not p:
        continue
      __ cmd == 0:
        k -= 1
        __ k == 0:
          return p.val
      else:
        stack.append((1, p.right))
        stack.append((0, p))
        stack.append((1, p.left))
