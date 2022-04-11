# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
_______ c..


c_ Solution(o..
  ___ findLeaves  root
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    ___ helper(p, res
      __ n.. p:
        r.. 0
      left helper(p.left, res)
      right helper(p.right, res)
      depth m..(left, right) + 1
      res[depth].a..(p.val)
      r.. depth

    ans    # list
    res c...d..(l..)
    helper(root, res)
    ___ i __ r..(1, l..(res) + 1
      ans.a..(res[i])
    r.. ans
