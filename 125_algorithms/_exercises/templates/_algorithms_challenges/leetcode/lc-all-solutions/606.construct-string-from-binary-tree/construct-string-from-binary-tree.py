c_ Solution(o..):
  ___ tree2str  t):
    """
    :type t: TreeNode
    :rtype: str
    """
    __ n.. t:
      r.. ""
    res = ""
    left = tree2str(t.left)
    right = tree2str(t.right)
    __ left o. right:
      res += "(%s)" % left
    __ right:
      res += "(%s)" % right
    r.. s..(t.val) + res
