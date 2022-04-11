# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
  ___ getMinimumDifference  root
    """
    :type root: TreeNode
    :rtype: int
    """
    val N..
    ans f__("inf")

    ___ inorder(root
      __ n.. root:
        r..
      inorder(root.left)
      __ val __ n.. N..
        ans m..(ans, a..(root.val - val
      val root.val
      inorder(root.right)

    inorder(root)
    r.. ans
