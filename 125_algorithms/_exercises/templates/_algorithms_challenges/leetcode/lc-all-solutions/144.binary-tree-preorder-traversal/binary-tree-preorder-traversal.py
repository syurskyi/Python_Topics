# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ preorderTraversal  root
    res, stack    # list, [(1, root)]
    w.... stack:
      p stack.p.. )
      __ n.. p[1]: _____
      stack.e.. [(1, p[1].right), (1, p[1].left), (0, p[1])]) __ p[0] !_ 0 ____ res.a..(p[1].val)
    r.. res
