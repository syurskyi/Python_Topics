class Solution(object):
  ___ tree2str(self, t):
    """
    :type t: TreeNode
    :rtype: str
    """
    __ n.. t:
      r.. ""
    res = ""
    left = self.tree2str(t.left)
    right = self.tree2str(t.right)
    __ left o. right:
      res += "(%s)" % left
    __ right:
      res += "(%s)" % right
    r.. s..(t.val) + res
