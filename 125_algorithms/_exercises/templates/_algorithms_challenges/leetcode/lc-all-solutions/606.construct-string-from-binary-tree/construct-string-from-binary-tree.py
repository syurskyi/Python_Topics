class Solution(object
  ___ tree2str(self, t
    """
    :type t: TreeNode
    :rtype: str
    """
    __ not t:
      r_ ""
    res = ""
    left = self.tree2str(t.left)
    right = self.tree2str(t.right)
    __ left or right:
      res += "(%s)" % left
    __ right:
      res += "(%s)" % right
    r_ str(t.val) + res
