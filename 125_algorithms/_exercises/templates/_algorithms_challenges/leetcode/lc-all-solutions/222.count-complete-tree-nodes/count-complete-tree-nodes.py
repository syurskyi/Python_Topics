# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ getHeight(self, root
    height = 0
    w___ root:
      height += 1
      root = root.left
    r_ height

  ___ countNodes(self, root
    count = 0
    w___ root:
      l, r = map(self.getHeight, (root.left, root.right))
      __ l __ r:
        count += 2 ** l
        root = root.right
      ____
        count += 2 ** r
        root = root.left
    r_ count
