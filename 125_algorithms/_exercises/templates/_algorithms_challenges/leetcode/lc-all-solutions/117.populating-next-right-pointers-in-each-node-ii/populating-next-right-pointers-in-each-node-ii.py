# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
  # @param root, a tree link node
  # @return nothing
  ___ connect(self, root):
    p = root
    pre = None
    head = None
    while p:
      __ p.left:
        __ pre:
          pre.next = p.left
        pre = p.left
      __ p.right:
        __ pre:
          pre.next = p.right
        pre = p.right
      __ not head:
        head = p.left or p.right
      __ p.next:
        p = p.next
      else:
        p = head
        head = None
        pre = None
