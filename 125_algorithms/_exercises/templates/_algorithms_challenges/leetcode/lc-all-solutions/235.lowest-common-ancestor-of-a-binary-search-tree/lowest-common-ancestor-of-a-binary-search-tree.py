c_ Solution(object):
  ___ lowestCommonAncestor  root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    a, b = s..([p.val, q.val])
    w.... n.. a <= root.val <= b:
      __ a > root.val:
        root = root.right
      ____:
        root = root.left
    r.. root
