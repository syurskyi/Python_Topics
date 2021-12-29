# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ preorderTraversal(self, root):
    res, stack = [], [(1, root)]
    while stack:
      p = stack.pop()
      __ not p[1]: continue
      stack.extend([(1, p[1].right), (1, p[1].left), (0, p[1])]) __ p[0] != 0 else res.append(p[1].val)
    return res
