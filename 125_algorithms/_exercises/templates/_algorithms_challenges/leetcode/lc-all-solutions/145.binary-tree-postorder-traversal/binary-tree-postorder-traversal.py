# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res, stack    # list, [(1, root)]
    w.... stack:
      p = stack.pop()
      __ n.. p[1]:
        continue
      __ p[0] __ 0:
        res.a..(p[1].val)
      ____:
        stack.extend([(0, p[1]), (1, p[1].right), (1, p[1].left)])
    r.. res
