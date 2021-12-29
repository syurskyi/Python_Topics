# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ findDuplicateSubtrees(self, root):
    from hashlib import sha256
    ___ hash_(x):
      S = sha256()
      S.update(x)
      return S.hexdigest()

    ___ merkle(node):
      __ not node:
        return '#'
      m_left = merkle(node.left)
      m_right = merkle(node.right)
      node.merkle = hash_(m_left + str(node.val) + m_right)
      count[node.merkle].append(node)
      return node.merkle

    count = collections.defaultdict(list)
    merkle(root)
    return [nodes.pop() for nodes in count.values() __ len(nodes) >= 2]
