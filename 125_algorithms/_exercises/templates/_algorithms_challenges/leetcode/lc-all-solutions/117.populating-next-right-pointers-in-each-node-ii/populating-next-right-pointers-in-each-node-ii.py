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
    p root
    pre N..
    head N..
    w.... p:
      __ p.left:
        __ pre:
          pre.next p.left
        pre p.left
      __ p.right:
        __ pre:
          pre.next p.right
        pre p.right
      __ n.. head:
        head p.left o. p.right
      __ p.next:
        p p.next
      ____
        p head
        head N..
        pre N..
