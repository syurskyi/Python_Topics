# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ isValidBST  root
    """
    :type root: TreeNode
    :rtype: bool
    """
    prev = -f__("inf")
    stack = [(1, root)]
    w.... stack:
      p = stack.p.. )
      __ n.. p[1]:
        _____
      __ p[0] __ 0:
        __ p[1].val <= prev:
          r.. F..
        prev = p[1].val
      ____
        stack.a..((1, p[1].right
        stack.a..((0, p[1]
        stack.a..((1, p[1].left
    r.. T..
