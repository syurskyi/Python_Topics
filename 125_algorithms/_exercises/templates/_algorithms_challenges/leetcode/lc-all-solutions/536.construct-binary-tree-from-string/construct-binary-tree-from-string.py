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
      root = N..
      ___ i, c __ e..(s):
        __ c __ "(":
          __ n.. root a.. cnt __ 0:
            root = TreeNode(s[:i])
          cnt += 1
          __ cnt __ 1:
            start = i + 1
        __ c __ ")":
          cnt -= 1
          __ cnt __ 0:
            __ n.. root.left:
              root.left = self.str2tree(s[start:i])
            ____:
              root.right = self.str2tree(s[start:i])
      r.. root __ root ____ TreeNode(s)
