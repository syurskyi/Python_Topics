# Definition for a  binary tree node
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object
  ___ __init__(self, root
    """
    :type root: TreeNode
    """
    self.p = None
    self.stack = []
    __ root:
      self.stack.append((1, root))

  ___ hasNext(self
    """
    :rtype: bool
    """
    r_ le.(self.stack) > 0

  ___ next(self
    """
    :rtype: int
    """
    stack = self.stack
    w___ stack:
      p = stack.pop()
      __ not p[1]:
        continue
      __ p[0] __ 0:
        r_ p[1].val
      ____
        l = []
        __ p[1].right:
          l.append((1, p[1].right))
        l.append((0, p[1]))
        __ p[1].left:
          l.append((1, p[1].left))
        stack.extend(l)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# w___ i.hasNext( v.append(i.next())
