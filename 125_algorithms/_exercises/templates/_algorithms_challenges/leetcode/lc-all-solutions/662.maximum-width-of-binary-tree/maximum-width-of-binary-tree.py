c_ Solution(o..):
  ___ widthOfBinaryTree  root):
    """
    :type root: TreeNode
    :rtype: int
    """

    ___ dfs(root, x, y, num, dmin, dmax):
      __ root:
        left = dfs(root.left, x - 1, y + 1, num * 2, dmin, dmax)
        right = dfs(root.right, x + 1, y + 1, 1 + num * 2, dmin, dmax)
        dmin[y] = m..(num, dmin.get(y, float("inf")))
        dmax[y] = m..(num, dmax.get(y, float("-inf")))
        r.. m..(left o. 0, right o. 0, 1 + dmax[y] - dmin[y])

    r.. dfs(root, 0, 0, 1, {}, {})
