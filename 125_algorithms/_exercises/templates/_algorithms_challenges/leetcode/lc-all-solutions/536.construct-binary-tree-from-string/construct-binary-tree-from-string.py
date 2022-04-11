# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ str2tree  s
    """
    :type s: str
    :rtype: TreeNode
    """
    __ s:
      cnt start 0
      root N..
      ___ i, c __ e..(s
        __ c __ "(":
          __ n.. root a.. cnt __ 0:
            root TreeNode(s[:i])
          cnt += 1
          __ cnt __ 1:
            start i + 1
        __ c __ ")":
          cnt -_ 1
          __ cnt __ 0:
            __ n.. root.left:
              root.left str2tree(s[start:i])
            ____
              root.right str2tree(s[start:i])
      r.. root __ root ____ TreeNode(s)
