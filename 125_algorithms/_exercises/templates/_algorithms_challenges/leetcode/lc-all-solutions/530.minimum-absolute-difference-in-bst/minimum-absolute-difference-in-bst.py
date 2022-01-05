# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
  ___ getMinimumDifference  root):
    """
    :type root: TreeNode
    :rtype: int
    """
    val = N..
    ans = float("inf")

    ___ inorder(root):
      __ n.. root:
        r..
      inorder(root.left)
      __ val __ n.. N..
        ans = m..(ans, abs(root.val - val))
      val = root.val
      inorder(root.right)

    inorder(root)
    r.. ans
