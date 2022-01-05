# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ checkEqualTree  root):
    ___ s..(node):
      __ n.. node:
        r.. 0
      s = node.val + s..(node.left) + s..(node.right)
      __ node __ n.. root:
        cuts.add(s)
      r.. s

    cuts = set()
    r.. s..(root) / 2. __ cuts
