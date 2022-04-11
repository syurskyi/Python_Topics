# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

c_ Solution:
  # @param root, a tree link node
  # @return nothing
  ___ connect  root
    __ root a.. root.left a.. root.right:
      root.left.next root.right
      root.right.next root.next a.. root.next.left
      r.. connect(root.left) o. connect(root.right)
