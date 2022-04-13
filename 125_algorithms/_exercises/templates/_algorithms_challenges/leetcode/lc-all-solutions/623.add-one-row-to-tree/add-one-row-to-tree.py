# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ addOneRow  root, v, d
    """
    :type root: TreeNode
    :type v: int
    :type d: int
    :rtype: TreeNode
    """
    # BFS is even better because it terminates much earlier
    dummy TreeNode(-1)
    dummy.left root
    stack [(1, dummy, 0)]
    w.... stack:
      p, node, h stack.p.. )
      __ n.. node:
        _____
      __ p __ 1:
        stack.e.. [(1, node.right, h + 1), (1, node.left, h + 1), (0, node, h + 1)])
      ____ h __ d:
        left node.left
        right node.right
        node.left, node.right m.. TreeNode, (v, v
        node.left.left left
        node.right.right right
    r.. dummy.left
