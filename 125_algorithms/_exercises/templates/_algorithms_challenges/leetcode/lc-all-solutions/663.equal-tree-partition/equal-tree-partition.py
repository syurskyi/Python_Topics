# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ checkEqualTree(self, root
    ___ su.(node
      __ not node:
        r_ 0
      s = node.val + su.(node.left) + su.(node.right)
      __ node pa__ not root:
        cuts.add(s)
      r_ s

    cuts = set()
    r_ su.(root) / 2. in cuts
