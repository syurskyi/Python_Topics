# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ findDuplicateSubtrees  root
    ____ hashlib _______ sha256
    ___ hash_(x
      S = sha256()
      S.update(x)
      r.. S.hexdigest()

    ___ merkle(node
      __ n.. node:
        r.. '#'
      m_left = merkle(node.left)
      m_right = merkle(node.right)
      node.merkle = hash_(m_left + s..(node.val) + m_right)
      count[node.merkle].a..(node)
      r.. node.merkle

    count = c...d..(l..)
    merkle(root)
    r.. [nodes.p.. ) ___ nodes __ count.v.. __ l..(nodes) >_ 2]
