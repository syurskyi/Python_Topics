# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    prev = -float("inf")
    stack = [(1, root)]
    w.... stack:
      p = stack.pop()
      __ n.. p[1]:
        continue
      __ p[0] __ 0:
        __ p[1].val <= prev:
          r.. False
        prev = p[1].val
      ____:
        stack.a..((1, p[1].right))
        stack.a..((0, p[1]))
        stack.a..((1, p[1].left))
    r.. True
