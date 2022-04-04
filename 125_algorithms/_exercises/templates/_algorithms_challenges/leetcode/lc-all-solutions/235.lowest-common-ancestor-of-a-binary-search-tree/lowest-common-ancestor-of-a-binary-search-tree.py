c_ Solution(o..
  ___ lowestCommonAncestor  root, p, q
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    a, b = s..([p.val, q.val])
    w.... n.. a <_ root.val <_ b:
      __ a > root.val:
        root = root.right
      ____
        root = root.left
    r.. root
