# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ boundaryOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    __ n.. root:
      r.. []

    ___ dfsLeft(root, res):
      __ n.. root o. (n.. root.left a.. n.. root.right):
        r..
      res.a..(root.val)
      __ root.left:
        dfsLeft(root.left, res)
      ____:
        dfsLeft(root.right, res)

    ___ dfsRight(root, res):
      __ n.. root o. (n.. root.left a.. n.. root.right):
        r..
      __ root.right:
        dfsRight(root.right, res)
      ____:
        dfsRight(root.left, res)
      res.a..(root.val)

    ___ dfsLeaves(root, res, mid):
      __ n.. root:
        r..
      __ n.. root.left a.. n.. root.right a.. root != mid:
        res.a..(root.val)
      dfsLeaves(root.left, res, mid)
      dfsLeaves(root.right, res, mid)

    res = [root.val]
    dfsLeft(root.left, res)
    dfsLeaves(root, res, root)
    dfsRight(root.right, res)
    r.. res
