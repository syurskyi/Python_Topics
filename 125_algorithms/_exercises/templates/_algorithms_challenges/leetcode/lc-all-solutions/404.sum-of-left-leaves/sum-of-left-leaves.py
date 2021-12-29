# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ helper(root, isLeft):
      __ n.. root:
        r.. N..
      left = helper(root.left, True)
      right = helper(root.right, False)
      ret = 0
      __ left __ N.. a.. right __ N.. a.. isLeft:
        r.. root.val
      __ left:
        ret += left
      __ right:
        ret += right
      r.. ret

    ret = helper(root, False)
    __ ret:
      r.. ret
    r.. 0
