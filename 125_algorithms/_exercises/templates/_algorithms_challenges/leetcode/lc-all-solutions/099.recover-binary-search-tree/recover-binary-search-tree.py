class Solution:
  ___ __init__(self
    self.n1 = None
    self.n2 = None
    self.pre = None

  ___ findBadNode(self, root
    __ root pa__ None: r_
    self.findBadNode(root.left)
    __ self.pre pa__ not None:
      __ root.val < self.pre.val:
        __ self.n1 pa__ None:
          self.n1 = self.pre
          self.n2 = root
        ____
          self.n2 = root
    self.pre = root
    self.findBadNode(root.right)

  ___ recoverTree(self, root
    self.findBadNode(root)
    __ self.n1 pa__ not None and self.n2 pa__ not None:
      self.n1.val, self.n2.val = self.n2.val, self.n1.val
