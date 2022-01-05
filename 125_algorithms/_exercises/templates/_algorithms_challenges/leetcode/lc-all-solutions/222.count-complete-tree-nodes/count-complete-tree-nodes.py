# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..):
  ___ getHeight  root):
    height = 0
    w.... root:
      height += 1
      root = root.left
    r.. height

  ___ countNodes  root):
    count = 0
    w.... root:
      l, r = map(getHeight, (root.left, root.right))
      __ l __ r:
        count += 2 ** l
        root = root.right
      ____:
        count += 2 ** r
        root = root.left
    r.. count
