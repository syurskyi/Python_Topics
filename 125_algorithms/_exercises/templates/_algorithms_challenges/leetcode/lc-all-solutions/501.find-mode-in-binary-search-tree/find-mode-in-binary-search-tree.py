# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  ___ findMode(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    ___ visit(v):
      __ v != self.pre:
        self.pre = v
        self.cnt = 0
      self.cnt += 1
      __ self.cnt > self.maxFreq:
        self.maxFreq = self.cnt
        self.modeCnt = 1
      ____ self.cnt __ self.maxFreq:
        __ self.ans:
          self.ans[self.modeCnt] = v
        self.modeCnt += 1

    ___ inorder(root):
      __ root:
        inorder(root.left)
        visit(root.val)
        inorder(root.right)

    self.pre = N..
    self.ans = N..
    self.maxFreq = self.modeCnt = self.cnt = 0
    inorder(root)
    self.ans = [0] * self.modeCnt
    self.modeCnt = self.cnt = 0
    inorder(root)
    r.. self.ans
