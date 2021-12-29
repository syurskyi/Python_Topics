# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ str2tree(self, s):
    """
    :type s: str
    :rtype: TreeNode
    """
    __ s:
      cnt = start = 0
      root = None
      for i, c in enumerate(s):
        __ c == "(":
          __ not root and cnt == 0:
            root = TreeNode(s[:i])
          cnt += 1
          __ cnt == 1:
            start = i + 1
        __ c == ")":
          cnt -= 1
          __ cnt == 0:
            __ not root.left:
              root.left = self.str2tree(s[start:i])
            else:
              root.right = self.str2tree(s[start:i])
      return root __ root else TreeNode(s)
