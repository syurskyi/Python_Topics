# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ findDuplicateSubtrees(self, root
    from hashlib ______ sha256
    ___ hash_(x
      S = sha256()
      S.update(x)
      r_ S.hexdigest()

    ___ merkle(node
      __ not node:
        r_ '#'
      m_left = merkle(node.left)
      m_right = merkle(node.right)
      node.merkle = hash_(m_left + str(node.val) + m_right)
      count[node.merkle].append(node)
      r_ node.merkle

    count = collections.defaultdict(list)
    merkle(root)
    r_ [nodes.p.. ___ nodes __ count.values() __ le.(nodes) >= 2]
