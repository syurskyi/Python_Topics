class Solution(object):
  ___ tree2str(self, t):
    """
    :type t: TreeNode
    :rtype: str
    """
    __ not t:
      return ""
    res = ""
    left = self.tree2str(t.left)
    right = self.tree2str(t.right)
    __ left or right:
      res += "(%s)" % left
    __ right:
      res += "(%s)" % right
    return str(t.val) + res
