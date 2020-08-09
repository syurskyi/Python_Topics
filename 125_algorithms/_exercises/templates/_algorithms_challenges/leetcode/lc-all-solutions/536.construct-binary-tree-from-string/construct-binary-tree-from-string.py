# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
  ___ str2tree(self, s
    """
    :type s: str
    :rtype: TreeNode
    """
    __ s:
      cnt = start = 0
      root = None
      for i, c in enumerate(s
        __ c __ "(":
          __ not root and cnt __ 0:
            root = TreeNode(s[:i])
          cnt += 1
          __ cnt __ 1:
            start = i + 1
        __ c __ ")":
          cnt -= 1
          __ cnt __ 0:
            __ not root.left:
              root.left = self.str2tree(s[start:i])
            ____
              root.right = self.str2tree(s[start:i])
      r_ root __ root else TreeNode(s)
