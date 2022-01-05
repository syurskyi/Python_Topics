# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ inorderSuccessor  root, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :rtype: TreeNode
    """
    __ root a.. q:
      flag = F..
      stack = [(1, root)]
      w.... stack:
        p = stack.pop()
        __ n.. p[1]:
          _____
        __ p[0] __ 0:
          __ flag:
            r.. p[1]
          __ p[1] __ q:
            flag = T..
        ____:
          stack.extend([(1, p[1].right), (0, p[1]), (1, p[1].left)])

      r.. N..
