# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res, stack    # list, [(1, root)]
    while stack:
      p = stack.pop()
      __ n.. p[1]: continue
      stack.extend([(1, p[1].right), (0, p[1]), (1, p[1].left)]) __ p[0] != 0 ____ res.a..(p[1].val)
    r.. res
