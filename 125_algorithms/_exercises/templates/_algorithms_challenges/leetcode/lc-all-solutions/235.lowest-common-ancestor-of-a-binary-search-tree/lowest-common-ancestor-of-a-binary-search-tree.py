class Solution(object
  ___ lowestCommonAncestor(self, root, p, q
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    a, b = sorted([p.val, q.val])
    w___ not a <= root.val <= b:
      __ a > root.val:
        root = root.right
      ____
        root = root.left
    r_ root
