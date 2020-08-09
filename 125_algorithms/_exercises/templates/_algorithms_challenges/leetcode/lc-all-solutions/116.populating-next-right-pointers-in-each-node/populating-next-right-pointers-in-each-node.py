# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
  # @param root, a tree link node
  # @return nothing
  ___ connect(self, root
    __ root and root.left and root.right:
      root.left.next = root.right
      root.right.next = root.next and root.next.left
      r_ self.connect(root.left) or self.connect(root.right)
