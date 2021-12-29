class Solution:
  ___ __init__(self):
    self.n1 = N..
    self.n2 = N..
    self.pre = N..

  ___ findBadNode(self, root):
    __ root __ N.. r..
    self.findBadNode(root.left)
    __ self.pre __ n.. N..
      __ root.val < self.pre.val:
        __ self.n1 __ N..
          self.n1 = self.pre
          self.n2 = root
        ____:
          self.n2 = root
    self.pre = root
    self.findBadNode(root.right)

  ___ recoverTree(self, root):
    self.findBadNode(root)
    __ self.n1 __ n.. N.. a.. self.n2 __ n.. N..
      self.n1.val, self.n2.val = self.n2.val, self.n1.val
