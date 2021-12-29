# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
  ___ __init__(self, root):
    """
    :type root: TreeNode
    """
    self.p = N..
    self.stack    # list
    __ root:
      self.stack.a..((1, root))

  ___ hasNext(self):
    """
    :rtype: bool
    """
    r.. l..(self.stack) > 0

  ___ next(self):
    """
    :rtype: int
    """
    stack = self.stack
    while stack:
      p = stack.pop()
      __ n.. p[1]:
        continue
      __ p[0] __ 0:
        r.. p[1].val
      ____:
        l    # list
        __ p[1].right:
          l.a..((1, p[1].right))
        l.a..((0, p[1]))
        __ p[1].left:
          l.a..((1, p[1].left))
        stack.extend(l)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
