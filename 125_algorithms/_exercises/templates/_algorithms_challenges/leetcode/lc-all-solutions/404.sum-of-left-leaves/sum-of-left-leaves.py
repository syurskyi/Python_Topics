# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ sumOfLeftLeaves  root
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ helper(root, isLeft
      __ n.. root:
        r.. N..
      left = helper(root.left, T..)
      right = helper(root.right, F..)
      ret = 0
      __ left __ N.. a.. right __ N.. a.. isLeft:
        r.. root.val
      __ left:
        ret += left
      __ right:
        ret += right
      r.. ret

    ret = helper(root, F..)
    __ ret:
      r.. ret
    r.. 0
