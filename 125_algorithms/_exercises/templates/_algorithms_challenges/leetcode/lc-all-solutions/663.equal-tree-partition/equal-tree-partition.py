# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ checkEqualTree(self, root
    ___ sum(node
      __ not node:
        r_ 0
      s = node.val + sum(node.left) + sum(node.right)
      __ node is not root:
        cuts.add(s)
      r_ s

    cuts = set()
    r_ sum(root) / 2. in cuts
