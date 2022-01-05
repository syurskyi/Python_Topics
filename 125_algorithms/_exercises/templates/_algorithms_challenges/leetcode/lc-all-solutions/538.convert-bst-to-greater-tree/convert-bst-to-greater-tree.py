# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ - ):
    lSum = 0

  ___ convertBST  root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    __ n.. root:
      r.. N..
    convertBST(root.right)
    lSum += root.val
    root.val = lSum
    convertBST(root.left)
    r.. root
