# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ printTree(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[str]]
    """

    ___ height(root):
      __ n.. root:
        r.. 0
      r.. 1 + max(height(root.left), height(root.right))

    ___ fill(root, res, left, right, h):
      __ root:
        val = s..(root.val)
        mid = left + (right - left) / 2
        res[h][mid] = val
        fill(root.left, res, left, mid - 1, h + 1)
        fill(root.right, res, mid + 1, right, h + 1)

    h = height(root)
    res = [[""] * (2 ** h - 1) ___ _ __ r..(h)]
    fill(root, res, 0, l..(res[0]) - 1, 0)
    r.. res
